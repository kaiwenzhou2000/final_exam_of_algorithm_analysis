# 题目：有一批共n个集装箱要装上两艘载重量分别为c1和c2的轮船，
# 其中集装箱i的重量为wi，且集装箱总重量小于两艘船的载重总量。
# 请确定是否有一个合理的装载方案可将所有的集装箱装上这两艘轮船。
# 这是经典的装载问题，在此问题中，
# 当我们将问题变换成本质上是研究如何将第一艘船尽可能装满后，
# 在使用分支限界的方法时，是如何进行“分支限界”的？

# 思路：
# 首先将第一艘轮船尽最大可能装满
# 然后将剩余的集装箱装上第二艘轮船

# 表示第一艘船的最大负载重量
bestw: int = 50
# 表示物品的重量, 为了层数相互对应，在0索引的位置设置了一个哨兵节点
w = [-1, 10, 40, 40]
# w = [-1, 20, 40, 40]
# 表示现在所在的层数
level = 0
# 表示产生树的队列
queen = []
# 现在最大的容量
current_max = 0

# 先将整个树进行初始化
queen.append(0)
level += 1


def add_to_current_max(num):
    """
    :param num: 新进来的数字
    :return:    null
    """
    global current_max
    if num > current_max:
        current_max = num


# FIFO
def FIFO_not_cut():
    global level, queen, bestw, w
    while len(queen) != 0 and level < len(w):
        # 先取出头结点，作为根，分别有取和不取两种节点
        head = queen[0]
        # 取的情况，首先保证不超重
        if head + w[level] <= bestw:
            # 添加进入队列
            queen.append(head + w[level])
            # 与现在最大的比较
            add_to_current_max(head + w[level])

        # 不取的情况
        queen.append(head)
        level += 1
        del queen[0]


def FIFO_with_cut():
    global level, queen, bestw, w
    while len(queen) != 0 and level < len(w):
        # 先取出头结点，作为根，分别有取和不取两种节点
        head = queen[0]
        # 取的情况，首先保证不超重
        if head + w[level] <= bestw:
            # 添加进入队列
            queen.append(head + w[level])
            # 与现在最大的比较
            add_to_current_max(head + w[level])

        # 不取的情况
        temp = 0  # 计算分支上界
        for i in w[level: len(w)]:
            temp += i
        temp += head
        if temp > bestw:
            queen.append(head)
        level += 1
        del queen[0]


FIFO_with_cut()

print(current_max)
