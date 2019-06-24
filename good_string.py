def cal_good_string(n):
    if n.count('a') > len(n) / 2:
        return len(n)
    else:
        return cal_good_string(''.join(sorted(n))[:-1])


if __name__ == '__main__':
    n = input()
    i = cal_good_string(n)
    print(i)
