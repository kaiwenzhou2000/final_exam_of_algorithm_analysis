# 题目：在最长公共子序列问题中，
# 用c[i][j]记录Xi和Yi的最长公共子序列的长度。
# 其中，Xi={x1,x2…xi}，Yi={y1,y2…yi}。
# 当i或j的值为0时，X和Y的最长公共子序列为空序列。
# 请求出在一般情况下，由本问题的最优子结构性质所建立的递归关系式，给出推导过程。

s1 = [1, 3, 4, 5, 6, 7, 7, 8]
s2 = [3, 5, 7, 4, 8, 6, 7, 8, 2]

value_table = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]


def print_table():
    global value_table
    mat = "{:^5}"
    for i in value_table[1:]:
        for j in i[1:]:
            print(mat.format(j), end='')
        print()


for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            value_table[i][j] = value_table[i - 1][j - 1] + 1
        else:
            value_table[i][j] = max(value_table[i][j - 1], value_table[i - 1][j])

print_table()

