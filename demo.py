import os
import sys
import hashlib
import threading
import time

# 0, 56371972 --> binary
# 56371973, 112743944,

# C:/Users/divya.d/Pictures/Unresolved_issues.jpg --> 0, 30720
# C:/Users/divya.d/Pictures/Unresolved_issues_bkp.jpg -> 30721, 61440

# C:/Users/divya.d/django_tests
# C:/Users/divya.d/django_tests_bkp

FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/debug.log'
DEST_FILE = '/home/afour/PycharmProjects/Trillio_Files_Operations/logs/debug_bkp.log'


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "r") as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash_md5.update(str(chunk).encode('utf-8'))
    return hash_md5.hexdigest()


def size_of_file(fp):
    # returns the size of file in bytes.
    return fp.seek(0, 2)


def num_threads_creation(size):
    # Logic to create num of threads.
    power = 2 ** 10
    n = 0

    while size > power:
        size /= power
        n += 1
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 8
    if n == 4:
        return 16
    if n == 5:
        return 32


def progress(outer):
    def inner(**kwargs):
        print(kwargs)
        start = time.time()
        end = time.time()
    return inner


def read_in_chunks(fp, end_chunk, small_chunk_size=1000):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while small_chunk_size <= end_chunk:
        data = fp.read(small_chunk_size)
        if not data:
            break
        end_chunk -= small_chunk_size
        yield data


def read_file(fp, start_chunk, end_chunk, dest_fp):
    fp.seek(start_chunk)
    count = 0
    # data = fp.read(end_chunk)
    chunks = end_chunk - start_chunk
    data = read_in_chunks(fp, chunks)

    for piece in data:
        dest_fp.seek(start_chunk + count * len(piece))
        count += 1
        print('{} chunks completed.'.format(count * len(piece)))
        dest_fp.write(piece)
        progres = (count * len(piece) / chunks) * 100
        print('{}:- {} % completed out of {} bytes.'.format(threading.current_thread().name, progres, end_chunk))

    print('write completed.')


if __name__ == '__main__':
    start = time.time()
    hash_src_file = md5(FILE)
    print(hash_src_file)
    fp1 = open(FILE, 'r')
    fp2 = open(FILE, 'r')
    dest_fp_1 = open(DEST_FILE, 'w')
    dest_fp_2 = open(DEST_FILE, 'w')

    print(size_of_file(fp1))
    print(size_of_file(fp2))

    t1 = threading.Thread(target=read_file, args=(fp1, 0, size_of_file(fp1)//2, dest_fp_1))
    t2 = threading.Thread(target=read_file, args=(fp2, size_of_file(fp1)//2+1, size_of_file(fp1), dest_fp_2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    hash_dest_file = md5(DEST_FILE)
    print(hash_dest_file)
    end = time.time()
    if hash_src_file == hash_dest_file:
        print('Copied Successfully in {} time.'.format(end - start))
    else:
        print('corrupted in {}'.format(end - start))
