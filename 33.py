




m,n = input().split()
m = int(m)
n = int(n)

data = {}
a = []
for i in range(m):
    cc,dd = input().split()
    cc = int(cc)
    dd = int(dd)
    data[cc]=dd
for i in range(n):
    a.append(int(input()))

bb = [i for i in data.keys()]
for i in a:
    if i in data:
        print(data[i])
    else:
        aa = [i - 9 for i in bb]
        aa.sort()
        for j in aa:
            if j > 0:
                print(data[bb[index]])
                break