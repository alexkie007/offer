def replaceString(str):
    str = str.replace(' ', '%20')
    return str


import re
def replaceString1(str):
    ret = re.compile(' ')
    str = ret.sub('%20', str)
    return str

def replaceString2(str):
    string = list(str)
    replaceStr = []
    for item in string:
        if item == ' ':
            replaceStr.append('%20')
        else:
            replaceStr.append(item)

    return "".join(replaceStr)
print(replaceString2('   s d ds '))