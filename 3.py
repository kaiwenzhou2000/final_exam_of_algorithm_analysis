# 题目：
# 给定n种物品和一个背包。物品i的重量为wi，其价值为vi,
# 背包的容量为C。使用动态规划方法分析并描述应该如何选择装入背包的物品，
# 使得装入背包中物品的总价值最大？在选择装入背包时，
# 对每种物品只有两种选择：即装入背包或不装入背包，不能将物品装入背包多次，也不能只装入部分某物品。

value = [-1, 3000, 2000, 1500]  # 价值列表
weight = [-1, 4, 3, 1]  # 重量列表
n = len(weight)-1       # n是物品的个数
c = 4                   # 书包的重量
value_table = [[0 for i in range(c + 1)] for j in range(n + 1)]     # 价值表

def print_table():
    global value_table
    mat = "{:^10}"
    for i in value_table[1:len(value_table)]:
        for j in i[1:len(i)]:
            print(mat.format(j), end='')
        print()


for i in range(1, n+1):
    for j in range(1, c+1):
        take = 0
        not_take = 0
        # 计算拿了之后的价值
        if weight[i] <= j:
            take = value[i] + value_table[i-1][j-weight[i]]
        # 计算不拿之后的价值
        not_take = value_table[i-1][j]
        # 比较是拿了之后的价值大还是不拿的价值高
        if take < not_take:
            value_table[i][j] = not_take
        else:
            value_table[i][j] = take


print_table()
