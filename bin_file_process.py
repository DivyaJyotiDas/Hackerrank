import os
import sys
import hashlib
import threading
from multiprocessing import Process
import time

# 0, 56371972 --> binary
# 56371973, 112743944,

# C:/Users/divya.d/Pictures/Unresolved_issues.jpg --> 0, 30720
# C:/Users/divya.d/Pictures/Unresolved_issues_bkp.jpg -> 30721, 61440

# FILE = 'C:/Users/divya.d/PycharmProjects/kvm_project/debug.log'
# DEST_FILE = 'C:/Users/divya.d/PycharmProjects/kvm_project/debug_bkp.log'


# C:/Users/divya.d/django_tests
# C:/Users/divya.d/django_tests_bkp

FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/dm-1'
T1_DEST_FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/backup_one.img'
T2_DEST_FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/backup_two.img'

# FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/debug.log'
# T1_DEST_FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/backup_one.img'
# T2_DEST_FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/backup_two.img'


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def size_of_file(fp):
    # returns the size of file in bytes.
    return fp.seek(0, 2)


def num_process_creation(size):
    # Logic to create num of threads.
    power = 2 ** 10
    n = 0

    while size > power:
        size /= power
        n += 1

    return pow(2, n)


def execution_time(outer):
    """

    :param outer:
    :return:
    """
    def inner(fp, start_chunk, end_chunk, dest_fp):
        start_time = time.time()
        outer(fp, start_chunk, end_chunk, dest_fp)
        end_time = time.time()
        print(end_time - start_time)

    return inner


def read_in_chunks(fp, start_chunk, end_chunk, small_chunk_size=1000000):
    """
        Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k.

        Smart way of generating data on fly rather keeping all data in memory
    """

    num = 1
    while end_chunk >= num * small_chunk_size:
        data = fp.read(small_chunk_size)
        if not data:
            break
        num += 1
        yield data

    yield fp.read(abs(end_chunk - (num - 1) * small_chunk_size))


@execution_time
def read_file(fp, start_chunk, end_chunk, dest_fp):
    """

    :param fp:
    :param start_chunk:
    :param end_chunk:
    :param dest_fp:
    :return:
    """
    progress, count = 0, 0
    fp.seek(start_chunk)
    dest_fp.seek(start_chunk)

    chunks = end_chunk - start_chunk
    data = read_in_chunks(fp, start_chunk, end_chunk)

    for piece in data:
        count += 1
        dest_fp.write(piece)
        progress += (len(piece) / chunks) * 100
        print('{}:- {} % completed out of {} bytes.'.format(threading.current_thread().name, progress, end_chunk))

    print('write completed.')


if __name__ == '__main__':
    start = time.time()
    hash_src_file = md5(FILE)
    print(hash_src_file)
    fp1 = open(FILE, 'rb')
    fp2 = open(FILE, 'rb')
    dest_fp_1 = open(T1_DEST_FILE, 'wb')
    dest_fp_2 = open(T1_DEST_FILE, 'wb')

    print(size_of_file(fp1))
    print(size_of_file(fp2))

    p1 = Process(target=read_file, args=(fp1, 0, size_of_file(fp1) // 2, dest_fp_1))
    p2 = Process(target=read_file, args=(fp2, size_of_file(fp1) // 2, size_of_file(fp1), dest_fp_2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # t1 = threading.Thread(target=read_file, args=(fp1, 0, 1023410176, dest_fp_1))
    # t2 = threading.Thread(target=read_file, args=(fp2, 511705089, 1023410176, dest_fp_2))

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    hash_dest_file = md5(T1_DEST_FILE)
    print(hash_dest_file)
    end = time.time()
    if hash_src_file == hash_dest_file:
        print('Copied Successfully in {} time.'.format(end - start))
    else:
        print('corrupted in {}'.format(end - start))
