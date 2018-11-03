'''
有一个整形数组arr和一个大小为w的窗口从数组的左边滑到最右边，
窗口每次向右边滑一个位置
'''


class Solution:
    def getMaxWindow(self, arr, w):
        if w > len(arr) or arr == None or w < 1:
            return

        deque = []
        res = []
        for i in range(len(arr)):
            while deque and arr[deque[-1]] <= arr[i]:
                deque.pop()
            deque.append(i)
            if deque[0] <= i - w:
                deque.pop(0)
            if i - w + 1 >= 0:
                res.append(arr[deque[0]])
        return res
