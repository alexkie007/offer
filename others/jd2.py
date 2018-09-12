class Solution:
    def is_com(self, nums):
        node_set = set()
        for i in nums:
            node_set.add(i[0])
            node_set.add(i[1])
        start_node = node_set.pop()
        count = 0
        while len(nums) > 0:
            start_edge = []
            for edge in nums:
                if edge[0] == start_node or edge[1] == start_node:
                    start_edge = edge
                    break
            if len(start_edge) == 0:
                break
            if start_edge[0] == start_node:
                end_node = start_edge[1]
                count += 1
                nums.remove(start_edge)
            elif start_edge[1] == start_node:
                count += 1
                end_node = start_edge[0]
                nums.remove(start_edge)
            start_node = end_node
        if count >= len(node_set) - 1 and len(nums) == 0:
            return "NO"
        return "YES"


s = Solution()
t = int(input())
result = []
for i in range(t):
    nam = input().split(" ")
    n = int(nam[0])
    m = int(nam[1])
    nums = []
    for j in range(m):
        nums.append([int(x) for x in input().split(" ")])
    result.append(s.is_com(nums))
for i in result:
    print(i)
