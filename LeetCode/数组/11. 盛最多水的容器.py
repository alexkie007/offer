"""
给定 n 个正整数 a1，a2，...，an，其中每个点的坐标用（i, ai）表示。
画 n 条直线，使得线 i 的两个端点处于（i，ai）和（i，0）处。请找出其中的两条直线，使得他们与 X 轴形成的容器能够装最多的水。



注意：你不能倾斜容器，n 至少是2。
"""

class Solution:
    def maxArea(self, height):
        length = len(height)
        low = 0
        high = length -1
        maxArea = 0
        while low < high:
            maxArea = max(maxArea, (high-low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxArea