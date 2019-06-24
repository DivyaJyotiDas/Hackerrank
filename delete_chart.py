import time


def removed_character(f_name):

    x_count = 0
    del_count = 0
    for i in f_name:
        if i == 'x':
            x_count += 1
        else:
            x_count = 0
        if x_count >= 3:
            del_count += 1

    return del_count


if __name__ == '__main__':
    #start = int(round(time.time() * 1000))
    n = int(input())
    f_name = input()
    res = removed_character(f_name)
    #end = int(round(time.time() * 1000))
    #print(end - start)
    print(res)