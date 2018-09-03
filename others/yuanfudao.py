# first = input()
# second = input()
first = "8 3"
second = "1 2 3 4 5 6 7 8"
numbers = first.split(" ")[0]
vol = int(first.split(" ")[1])
order = [int(x) for x in second.split(" ")]
result = []
count = 0
line = []
for index in range(0, len(order)):
    count += 1
    line.append(order[index])
    if count == vol or index == len(order) -1:
        result.append(line)
        line = []
        count = 0
result = result[::-1]
results = []
for x in result:
    for y in x:
        results.append(y)
print(" ".join([ str(x) for x in results]))
