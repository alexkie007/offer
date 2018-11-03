def cal_str(s):
    s = s.lower()
    map = {}
    for i in s:
        if i in map:
            map[i] = map[i]+1
        else:
            map[i] = 1
    for key,value in map.items():
        string = key+":"+str(value)
        print(string)

cal_str("a b A v")
