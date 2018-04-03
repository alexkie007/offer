"""
有两个大小为 m 和 n 的排序数组 nums1 和 nums2 。

请找出两个排序数组的中位数并且总的运行时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0


示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""
"""
解题思路：
这道题让我们求两个有序数组的中位数，而且限制了时间复杂度为O(log (m+n))，
看到这个时间复杂度，自然而然的想到了应该使用二分查找法来求解。但是这道题被定义为Hard也是有其原因的，
难就难在要在两个未合并的有序数组之间使用二分法，这里我们需要定义一个函数来找到第K个元素，
由于两个数组长度之和的奇偶不确定，因此需要分情况来讨论，对于奇数的情况，直接找到最中间的数即可，偶数的话需要求最中间两个数的平均值。
下面重点来看如何实现找到第K个元素，首先我们需要让数组1的长度小于或等于数组2的长度，
那么我们只需判断如果数组1的长度大于数组2的长度的话，交换两个数组即可，
然后我们要判断小的数组是否为空，为空的话，
直接在另一个数组找第K个即可。
还有一种情况是当K = 1时，表示我们要找第一个元素，只要比较两个数组的第一个元素，返回较小的那个即可。
如果数组a的中位数小于数组b的中位数，那么整体的中位数只可能出现在a的右区间加上b的左区间之中； 
如果数组a的中位数大于等于数组b的中位数，那么整体的中位数只可能出现在a的左区间加上b的右区间之中。 
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        return self.findKth(nums1, nums2, l // 2) if l % 2 == 1 else (self.findKth(nums1, nums2, l // 2 - 1) + self.findKth(nums1, nums2, l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = (B, A)
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])

        i = min(len(A) - 1, k / 2)
        j = min(len(B) - 1, k - i)

        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)

