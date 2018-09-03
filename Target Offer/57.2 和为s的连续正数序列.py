'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?
Good Luck!
'''


class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        mid = (1 + tsum) / 2
        curSum = small + big
        result = []
        while small < mid:
            if curSum == tsum:
                result.append(self.PrintContinuousSequence(small, big))
            while curSum > tsum and small < mid:
                curSum -= small
                small += 1
                if curSum == tsum:
                    result.append(self.PrintContinuousSequence(small, big))
            big += 1
            curSum += big

        return result

    def PrintContinuousSequence(self, small, big):
        res = []
        for i in range(small, big + 1):
            res.append(i)
        return res


s = Solution()
print(s.FindContinuousSequence(3))
