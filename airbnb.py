def paginate(resultsPerPage, results):
    is_add = [0 for i in range(len(results))]
    count = 0
    index_list = []
    output = []
    space_num = len(results) / resultsPerPage
    index = 0
    while len(output) != len(results) + space_num and index <= len(results)-1:
        host_info = results[index].replace("\"", "").split(",")
        host_index = host_info[0]
        if is_add[index] == 1:
            index += 1
            continue
        if host_index in index_list and index < len(results) - 1:
            index += 1
            continue
        if host_index in index_list and index == len(results) - 1:
            index = 0
            index_list = []
            continue
        output.append(results[index])
        is_add[index] = 1
        index_list.append(host_index)
        index += 1
        count += 1
        if count == resultsPerPage:
            output.append("")
            index_list = []
            count = 0
            if index == len(results) - 1:
                index = 0
            for i, v in enumerate(is_add):
                if v == 0:
                    index = i
                    break
    return output


results = [
    "1,28,300.6,San Francisco",
    "4,5,209.1,San Francisco",
    "20,7,203.4,Oakland",
    "6,8,202.9,San Francisco",
    "6,10,199.8,San Francisco",
    "1,16,190.5,San Francisco",
    "6,29,185.3,San Francisco",
    "7,20,180.0,Oakland",
    "6,21,162.2,San Francisco",
    "2,18,161.7,San Jose",
    "2,30,149.8,San Jose",
    "3,76,146.7,San Francisco",
    "2,14,141.8,San Jose"
]

results1 = [
    "1,28,100.3,Paris",
    "4,5,99.2,Paris",
    "2,7,90.5,Paris",
    "8,8,87.6,Paris",
    "6,10,85.6,Paris",
    "3,16,82.1,Paris",
    "7,29,81.1,Paris",
    "9,20,78.9,Paris",
    "12,21,74.3,Paris"
]

results2 = [
    "1,28,100.3,Paris",
    "4,5,99.2,Paris",
    "2,7,90.5,Paris",
    "8,8,87.6,Paris",
    "6,10,85.6,Paris",
    "3,16,82.1,Paris",
    "7,29,81.1,Paris",
    "9,22,80.0,Paris",
    "12,34,76.5,Paris"
]

output = paginate(4, results2)
for i in output:
    print(i)
