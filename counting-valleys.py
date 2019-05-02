

# Complete the countingValleys function below.
def countingValleys(str):
    bal_factor = 0
    start = ''
    mountain = 0
    valley = 0

    for i in str:
        if bal_factor == 0:
            start = i
            if start.lower() == 'u':
                bal_factor += 1
                mountain += 1
                continue
            if start.lower() == 'd':
                bal_factor -= 1
                valley += 1
                continue
        if bal_factor != 0:
            bal_factor = check_mountain_valley(bal_factor, i)

    return valley


def check_mountain_valley(bal_factor, i):
    if bal_factor >= 1:
        if i.lower() == 'u':
            bal_factor += 1
            return bal_factor

        if i.lower() == 'd':
            bal_factor -= 1
            return bal_factor

    if bal_factor <= -1:
        if i.lower() == 'u':
            bal_factor += 1
            return bal_factor

        if i.lower() == 'd':
            bal_factor -= 1
            return bal_factor

if __name__ == '__main__':
    #n = int(input())
    s = input()

    result = countingValleys(s)
    print(result)