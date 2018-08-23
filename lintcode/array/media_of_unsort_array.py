import heapq


class Solution:
    @staticmethod
    def median_of_unsort_array(nums):
        size = len(nums)
        heap = []
        for num in nums:
            num = -1 * num
            if len(heap) <= size // 2:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return -heap.pop(0)


s = Solution()
print(s.median_of_unsort_array([3, 1, 2, 4, 5]))
