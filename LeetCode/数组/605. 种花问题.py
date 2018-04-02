"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
"""


"""

找到不能种花的集中情况， 然后统计能种花的位置数量是否大于给定参数
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        ss =  ''.join(map(str,flowerbed))
        s = ss.replace('010', 'a').replace('10','b').replace('01', 'c').replace('00', '0a')
        return s.count('0') >= n
