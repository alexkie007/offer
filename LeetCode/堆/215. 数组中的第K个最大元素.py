"""
在未排序的数组中找到第 k 个最大的元素。请注意，它是数组有序排列后的第 k 个最大元素，而不是第 k 个不同元素。

例如，
给出 [3,2,1,5,6,4] 和 k = 2，返回 5。

注意事项:

你可以假设 k 总是有效的，1 ≤ k ≤ 数组的长度。
"""

"""
创建一个堆，弹出堆的第一个元素
"""
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for i in nums:
            if len(heap) >=  k:
                heapq.heappushpop(heap, i)
            else:
                heapq.heappush(heap, i )
        return heap[0]

s = Solution()
print(s.findKthLargest([3, 2,1,5,6,4] , 2))