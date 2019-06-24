def marcsCakewalk(calorie):
    sum = 0
    for i in range(len(calorie)):
        sum += pow(2, i) * calorie[i]
    return sum

if __name__ == '__main__':
    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie.sort(reverse=True))

    print(result)