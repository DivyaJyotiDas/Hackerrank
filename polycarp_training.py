def search_for_nearest(i, l):
    for j in range(i, len(l)+1):
        if l[i-1] > j:
            return i-1, l[i-1]


def training(l):
    new_l = []
    count = 0
    for i in range(1, len(l)+1):
        if i in l:
            ind = l.index(i)
            count += 1
            del l[ind]
        else:
            ret = search_for_nearest(i, l)
            if ret is not None:
                count += 1
                del l[ret[0]]
        print(l)
    return count


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = training(l)
    print(count)