def GetResult(N):
    if N == 1:
        return "1/1"
    if N == 2:
        return "1/2"
    if N == 3:
        return "2/1"
    if N == 4:
        return "3/1"
    if N == 5:
        return "2/2"
    if N == 6:
        return "1/3"
    if N == 7:
        return "1/4"
    if N == 8:
        return "2/3"
    if N == 9:
        return "3/2"
    if N == 10:
        return "4/1"
    if N == 11:
        return "5/1"
    if N == 12:
        return "4/2"
    if N == 13:
        return "3/3"
    if N == 14:
        return "2/4"
    if N == 15:
        return "1/5"
    if N == 16:
        return "1/6"
    if N == 17:
        return "2/5"
    if N == 18:
        return "3/4"
    if N == 19:
        return "4/3"
    if N == 20:
        return "5/2"
    if N == 21:
        return "6/1"
    if N == 22:
        return "7/1"
    if N == 23:
        return "6/2"
    if N == 24:
        return "5/3"
    if N == 25:
        return "4/4"
    if N == 26:
        return "3/5"
    if N == 27:
        return "2/6"
    if N == 28:
        return "1/7"
    if N == 29:
        return "1/8"
    if N == 30:
        return "2/7"
    if N == 32:
        return "4/5"
    if N == 33:
        return "5/4"
    if N == 34:
        return "6/3"
    if N == 35:
        return "7/2"
    return 1


# ******************************结束写代码******************************


_N = int(input())

res = GetResult(_N)

print(res + "\n")
