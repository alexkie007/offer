

def firstOne(str):
    hash = {}
    for i in str:
        hash[i] = hash[i]+1 if hash.get(i) else 1

    for i in str:
        if hash[i] == 1:
            return i

