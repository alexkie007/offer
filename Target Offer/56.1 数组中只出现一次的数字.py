'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        array.sort()
        result = []
        i = 0
        while i <= len(array) - 1:
            if i == len(array)-1:
                result.append(array[i])
                break
            if array[i] == array[i + 1]:
                i += 2
            else:
                result.append(array[i])
                i += 1

        return result


s = Solution()
print(s.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))