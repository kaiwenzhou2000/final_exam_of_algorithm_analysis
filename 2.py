# 题目
# 在2k*2k的棋盘覆盖问题中，如果k值等于3，
# 残缺方块的行列序号分别是7和6，
# 请给出此种状态下的覆盖过程描述并简单解释使用了何种算法
# 以及本题使用这种算法的优势。

# 分析
# 典型的分治法

k = 3
chess_board = [[-1 for i in range(2 ** k)] for j in range(2 ** k)]  # 二维列表渲染


# 展示棋盘
def print_chess_board():
    global chess_board
    chess_board[0][0] = 100
    for i in chess_board:
        for j in i:
            print(j, end=' ')
        print()


chess_board[7][6] = 0  # 标记缺少的位置


