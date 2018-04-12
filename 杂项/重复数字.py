class Solution:
    '''
    :param  n个数，数据范围[0,n-1]
    :return 重复数字
    '''
    def duplicateNums(self, numbers):
        if len(numbers) < 1:
            return
        for i in numbers:
            if i < 0 or i > len(numbers)-1:
                return
        duplicate = []
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplicate.append(numbers[i])
                    break
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
        return list(set(duplicate))

    '''
    :param  n个数，数据范围任意正整数
    :return 重复数字
    '''
    def duplicateNums2(self, numbers):
        ## 一个快指针，快指针每次走两步，慢指针每次走一步，找到他们的相交点
        if len(numbers) < 1:
            return -1
        slow = numbers[0]
        fast = numbers[numbers[0]]
        while slow != fast:
            slow = numbers[slow]
            fast = numbers[numbers[fast]]
        fast = 0
        while fast != slow:
            fast = numbers[fast]
            slow = numbers[slow]
        return slow

    def duplicateNums4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums[abs(i) - 1] < 0:
                return abs(i)
            nums[abs(i) - 1] = - nums[abs(i) - 1]





s=Solution()
print(s.duplicateNums2([2,3,5,4,2,6,2]))
print(s.duplicateNums4([2,3,5,4,2,6,2]))