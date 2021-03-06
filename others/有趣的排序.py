"""

度度熊有一个N个数的数组，他想将数组从小到大 排好序，但是萌萌的度度熊只会下面这个操作：
任取数组中的一个数然后将它放置在数组的最后一个位置。
问最少操作多少次可以使得数组从小到大有序？
输入描述:
首先输入一个正整数N，接下来的一行输入N个整数。(N <= 50, 每个数的绝对值小于等于1000)


输出描述:
输出一个整数表示最少的操作次数。
示例1
输入
4
19 7 8 25
输出
2


解题思路：

初始默认最小的元素是排好序的，然后判断第二小的元素，要是在最小的元素后面就是排好序的。如果第二个是排好序的再判断第三个，依次往后。
比如num含有 [4, 3, 1, 5, 2]。
 index得到的是[2, 4, 1, 0, 3]这样的。
2说明最小的是num[2]，4说明第二小是num[4]。
在num中，最小的数不用移动，然后第二小的数如果在最小的后面也不用移动。
第三小的如果在第二小的后面则不用移动。那么就是看index中，增加到哪里，
那就是保持上述规则不用移动的数。index里，4>1，意味num里第三小的数在第二小的之前，
所以必须移动一次。那么之后的都需要移动。
"""

nums = [19, 7, 8, 25]
index = sorted(range(len(nums)), key=lambda i:nums[i])
nums.sort()
count = 1
for i in range(1,len(nums)):
    if index[i] > index[i-1]:
        count += 1
    else:
        break

print(len(nums) - count)