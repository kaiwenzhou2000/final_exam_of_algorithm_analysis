# 题目：给定无向图G和m种不同的颜色，
# 用这些颜色对图G的各顶点进行着色，
# 每个顶点着一种颜色。
# 分析是否有一种着色法使G中每条边的两个顶点着不同颜色？
# 使用回溯法分析本问题，并画出在此框架下的解空间树（并添加适当注释）。

color_num = 3   # 颜色的数目
node_num: int = 3   # 节点的数目
G_map = [[1 for i in range(node_num)] for j in range(node_num)]  # 1表示是连通的
color_arr = [-1 for k in range(node_num)]   # 颜色数组

# G_map无向图的初始化
def G_map_ini():
    global G_map
    for i in range(node_num):
        for j in range(node_num):
            if i == j:
                G_map[i][j] = 0


def is_ok(node_index: int, color_index: int):
    """用来判断是不是不符合每条边的两个顶点着不同颜色这个条件
    :param node_index: 表示节点的编号
    :param color_index: 表示颜色的编号
    :return: True表示存在可以继续，False表示不可以继续
    """
    global G_map, node_num, color_arr
    for i in range(node_num):
        if G_map[node_index][i] == 1 and color_arr[i] == color_index:
            return False
    return True


def find_color(node_index: int):
    """使用递归来找到符合要求的图
    :param node_index: 表示节点的编号
    :return: 无
    """
    global G_map, node_num, color_arr
    # 函数递归的出口，到了叶子节点
    if node_index == node_num:
        print(color_arr)
    else:
        # 每个节点可以选择color_num中颜色
        for i in range(color_num):
            if is_ok(node_index, i):
                color_arr[node_index] = i
                find_color(node_index + 1)
                # 还原现场
                color_arr[node_index] = -1


G_map_ini()
find_color(0)
