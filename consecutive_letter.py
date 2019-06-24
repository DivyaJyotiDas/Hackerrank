
def get_val(s):
    for i in range(1, len(s)-1):
        d = list(s)
        if s[i] != s[i-1] and s[i] != s[i+1]:
            continue
        else:
            if s[i-1] > s[i+1]:
                d[i-1] = chr(ord(s[i-1]) + 1)
            if s[i-1] < s[i+1]:
                d[i-1] = chr(ord(s[i+1]) + 1)
            d = ''.join(d)

    return d


if __name__ == '__main__':
    s = input()
    s = get_val(s)
    print(s)