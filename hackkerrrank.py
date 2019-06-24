def hackerrankInString(s):
    """

    :rtype: string
    """
    l = ['h','a','c','k','e','r','r','a','n','k']
    flag = True
    temp = None
    str1 = ""
    for i in l:
        try:
            if i in s:
                str1 += s[s.index(i, temp)]
                temp = s.index(i, temp) + 1
            else:
                return "NO"
        except Exception as e:
            return "NO"


    if str1 == 'hackerrank':
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)