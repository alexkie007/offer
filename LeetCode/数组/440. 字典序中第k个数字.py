"""
给定整形数n和k，找到从1到n字典序中第k个数字。

提示: 1 ≤ k ≤ n ≤ 109.
例子：
输入:
n: 13   k: 2
输出:
10
解释:
字典序是[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 所以第二个数字是10.
"""
"""
解题思路：
因为字典序中全部是数字，所以我们可以将其看作是一个10叉树。
实这是个十叉树Denary Tree，就是每个节点的子节点可以有十个，比如数字1的子节点就是10到19，数字10的子节点可以是100到109，但是由于n大小的限制，构成的并不是一个满十叉树。
我们分析题目中给的例子可以知道，数字1的子节点有4个(10,11,12,13)，而后面的数字2到9都没有子节点，那么这道题实际上就变成了一个先序遍历十叉树的问题，
那么难点就变成了如何计算出每个节点的子节点的个数，我们不停的用k减去子节点的个数，
当k减到0的时候，当前位置的数字即为所求。现在我们来看如何求子节点个数，
比如数字1和数字2，我们要求按字典遍历顺序从1到2需要经过多少个数字，
首先把1本身这一个数字加到step中，然后我们把范围扩大十倍，范围变成10到20之前，
但是由于我们要考虑n的大小，由于n为13，所以只有4个子节点，
这样我们就知道从数字1遍历到数字2需要经过5个数字，
然后我们看step是否小于等于k，如果是，我们cur自增1，k减去step；
如果不是，说明要求的数字在子节点中，我们此时cur乘以10，k自减1，
以此类推，直到k为0推出循环，此时cur即为所求
"""
class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k -= 1
        while k > 0:
            step = 0
            first = cur
            last = cur + 1
            while first <= n:
                step += min(n+1, last) - first
                first *= 10
                last *= 10
            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -=1
        return cur
