"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算下雨之后能接多少雨水。

例如，
输入 [0,1,0,2,1,0,1,3,2,1,2,1]，返回 6。



上面的高度图由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示，在这种情况下，可以接 6 个单位的雨水（蓝色部分）。
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, water, minHeight = 0, n-1, 0, 0
        while l <r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l +=1
            while r >l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -=1
            minHeight = min(height[l], height[r])
        return water


