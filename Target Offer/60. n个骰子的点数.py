'''
扔 n 个骰子，向上面的数字之和为 S。
给定 Given n，请列出所有可能的 S 值及其相应的概率。
'''
class Solution:

    def dicesSum(self, n):
        if n == 0: return None
        result = [
            [1, 1, 1, 1, 1, 1],
        ]
        # if n == 1: return result[0]
        # 计算n个骰子出现的各个次数和
        for i in range(1, n):
            x = 5 * (i + 1) + 1
            result.append([0 for _ in range(x)])

            for j in range(x):
                if j < 6:
                    result[i][j] = (sum(result[i - 1][0:j + 1]))
                elif 6 <= j <= 3 * i + 2:
                    result[i][j] = (sum(result[i - 1][j - 5:j + 1]))
                else:
                    break
            left = 0
            right = len(result[i]) - 1
            while left <= right:
                result[i][right] = result[i][left]
                left += 1
                right -= 1

        res = result[-1]
        all = float(sum(res))
        other = []
        # 第i个元素代表骰子总和为n+i
        for i, item in enumerate(res):
            # pro = self.round(item/all)
            # 自己写的四舍五入算法和LintCode有出入，其实网站自身会处理数据，这里不再做处理
            pro = item / all
            other.append([n + i, pro])
        return other

    def round(self, num):
        # 将概率值四舍五入
        num = num * 100
        num = int(2 * num) / 2 + int(2 * num) % 2
        num = num / 100.0
        return num

s = Solution()
print(s.dicesSum(6))