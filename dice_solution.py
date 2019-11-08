def cal_adjancent(ele, i):
    adj_side = {
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    if adj_side[i] == ele:
        return False
    else:
        return True


def return_num_ways(ele, l):
    adj_count = 0
    for i in l:
        if ele == i:
            pass
        elif cal_adjancent(ele, i):
            adj_count += 1
        else:
            adj_count += 2
    return adj_count


def main():
    count = []
    l = list(map(int, input('Enter Dice Face')))
    for i in l:
        count.append(return_num_ways(i, l))

    print(min(count))


if __name__ == '__main__':
    main()
