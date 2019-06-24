def chess_winner(match):
    a_count = match.count('A')
    d_count = match.count('D')

    if a_count > d_count:
        return 'Anton'
    elif a_count < d_count:
        return 'Dalton'
    else:
        return 'Friendship'


if __name__ == '__main__':
    num = int(input())
    matches = input()
    res = chess_winner(matches)
    print(res)