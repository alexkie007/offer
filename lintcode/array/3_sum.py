class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if len(numbers) < 3:
            return []
        numbers.sort()
        res = set()
        for i, v in enumerate(numbers):
            if i >= 1 and v == numbers[i - 1]:
                continue
            d = {}
            for x in numbers[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add([v, -v - x, x])
        return res

    def threeSum2(self, numbers):
        # write your code here
        res = []
        numbers.sort()
        for i in range(len(numbers) - 1):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            l, r = i + 1, len(numbers) - 1
            while l < r:
                s = numbers[i] + numbers[l] + numbers[r]
                if s < 0:
                    l += 1
                elif s >0:
                    r -= 1
                else:
                    res.append((numbers[i], numbers[l], numbers[r]))
                    while l < r and numbers[l] == numbers[l + 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res