def isNumeric(s):
    if s == None or len(s) <= 0:
        return False

    aList = [w.lower() for w in s]
    if 'e' in aList:
        indexE = aList.index('e')
        front = aList[:indexE]
        behind = aList[indexE+1:]
        if '.' in behind or len(behind) == 0:
            return False

        isFront = scanDigit(front)
        isBehind = scanDigit(behind)
        return isBehind and isFront
    else:
        isnum = scanDigit(aList)
        return isnum


def scanDigit(list):
    dotNum = 0
    allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
    for i in range(len(list)):
        if list[i] not in allowVal:
            return  False
        if list[i] == '.':
            dotNum +=1
        if list[i] in '+-' and i !=0:
            return False
    if dotNum >1:
        return False
    return True

def isNumeric2(s):
    try:
        float(s)
        if s[0:2] != '-+' and s[0:2] != '+-':
            return True
        else:
            return False
    except:
        return False
print(isNumeric2('12e5'))