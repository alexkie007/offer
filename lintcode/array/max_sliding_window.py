import collections
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or k == 1:
            return nums
        if k > len(nums):
            return [max(nums)]
        deq, res = collections.deque() , []
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            # 判满
            if deq[0] == i - k:
                deq.popleft()
            # 取出窗口中最大的
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res