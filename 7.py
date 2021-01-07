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
# w = [-1, 10, 40, 40]
w = [-1, 10, 30, 50]
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


class node:

    def __init__(self, max, current_w, level):
        self.max = max          # 下面要是全部拿到的话一共有多少
        self.current_w = current_w      # 现在的重量
        self.level = level


# 大顶堆
class MaxHeap:
    def __init__(self):
        self.data = [node(-1, -1, -1)]
        self.size = 0

    def add(self, item):
        self.size += 1
        self.data.append(item)
        i = self.size
        while i != 1:
            j = int(i / 2)  # 父节点编号
            if self.data[j].max < self.data[i].max:
                # 交换父子节点
                temp = self.data[j]
                self.data[j] = self.data[i]
                self.data[i] = temp
                i = j
            else:
                break

    def pop(self):
        if self.size == 0:
            print('len = 0, can\'t pop')
            return
        self.data[1] = self.data[self.size]
        del self.data[self.size]
        self.size -= 1
        i = 1
        while i < self.size:
            # 找出左右的最大节点max_node
            left = i * 2  # 左节点下标
            right = i * 2 + 1  # 右节点下标
            # 左边越界
            if left > self.size:
                break
            # 右边越界
            if right > self.size:
                # 最大值是左边
                temp = self.data[i]
                self.data[i] = self.data[left]
                self.data[left] = temp
                i = left
                continue

            # 左右都没有越界
            if self.data[right].max > self.data[left].max:
                temp = self.data[i]
                self.data[i] = self.data[right]
                self.data[right] = temp
                i = right
            else:
                temp = self.data[i]
                self.data[i] = self.data[left]
                self.data[left] = temp
                i = left

    def show_queen(self):
        for i in self.data[1: self.size + 1]:
            print(str(i.max) + ' ', end='')


# LC-搜索
def LC_search():
    global level,current_max
    # 建立大根堆
    mh = MaxHeap()
    # 初始化树，建立根节点
    mh.add(node(0, 0, 0))
    head_level = 0
    level = head_level + 1
    while level != len(w) and mh.size != 0:
        print(head_level)
        temp = 0
        for i in w[level:]:
            temp += i
        # 找到E-节点
        head_current_w = mh.data[1].current_w
        mh.pop()
        # 左子节点
        if head_current_w + w[level] < bestw:
            # 更新current_max
            if current_max < head_current_w + w[level]:
                current_max = head_current_w + w[level]
            mh.add(node(temp, head_current_w + w[level], level))
        # 右子节点
        if current_max + temp-w[level] > bestw:
            mh.add(node(temp-w[level], head_current_w, level))

        # 更新下一个头的节点
        head_level = mh.data[1].level
        level = head_level + 1      # 叶子节点的层数
    print(current_max)

# FIFO_with_cut()
#
# print(current_max)

LC_search()

# mh = MaxHeap()
# mh.add(node(0, 0, 0))
# mh.pop()

