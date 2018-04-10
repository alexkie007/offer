"""
给定一个字符串S和有效单词的字典D，请确定可以插入到S中的最小空格数，使得最终的字符串完全由D中的有效单词组成，并输出解。

如果没有解则应该输出n/a

例如

输入
S = "ilikealibaba"
D = ["i", "like", "ali", "liba", "baba", "alibaba"]
Example Output:

输出
"i like alibaba"

解释：
字符串S可能被字典D这样拆分
"i like ali baba"
"i like alibaba"
很显然，第二个查分结果是空格数最少的解。
"""