'''
统计一个数字在排序数组中出现的次数。
例如，输入排序数组{12,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4。
'''


class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

    def GetNumberOfK2(self, data, k):
        length = len(data)
        if length == 0 or k > data[-1]:
            return 0
        if length == 1 and data[0] == k:
            return 1
        start = 0
        end = length - 1
        count = 0
        while start < end:
            mid = int((end - start) / 2)
            if data[mid] < k:
                start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                i = mid
                while data[i] == k and i >= 0:
                    count += 1
                    i -= 1
                i = mid + 1

                while i <= end and data[i] == k:
                    count += 1
                    i += 1
                break
        return count


class Solution1:
    def binary_sarch(self, data, k, is_left):
        s = 0
        e = len(data) - 1
        while s <= e:
            mid = (s + e) / 2
            if data[mid] > k:
                e = mid - 1
            elif data[mid] < k:
                s = mid + 1
            else:
                if is_left and mid != 0 and data[mid - 1] == k:
                    e = mid - 1
                elif not is_left and mid != len(data) - 1 and data[mid + 1] == k:
                    s = mid + 1
                else:
                    return mid
        return -1

    def GetNumberOfK(self, data, k):
        k_l = self.binary_sarch(data, k, True)
        k_r = self.binary_sarch(data, k, False)
        if k_l == -1 and k_r == -1:
            return 0
        return k_r - k_l + 1


# write code here


a = [1, 2, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetNumberOfK2(a, 3))
