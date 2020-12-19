# 题目
# 在2k*2k的棋盘覆盖问题中，如果k值等于3，
# 残缺方块的行列序号分别是7和6，
# 请给出此种状态下的覆盖过程描述并简单解释使用了何种算法
# 以及本题使用这种算法的优势。

# 分析
# 典型的分治法

k = 3
chess_board = [[-1 for i in range(2 ** k)] for j in range(2 ** k)]  # 二维列表渲染
missing_point = {'x': 6, 'y': 7}
chess_board[missing_point['x']][missing_point['y']] = 0  # 标记缺少的位置
step = 1  # 人工标记的特殊点


# 展示棋盘
def print_chess_board():
    global chess_board
    mat = "{:^3}"
    for i in chess_board:
        for j in i:
            print(mat.format(j), end=' ')
        print()


# size 指的是棋盘的大小
# chess_board_x 指的是当前棋盘左上的行的坐标
# chess_board_y 指的是当前棋盘左上的列的坐标
# missing_x 指的是缺失的格子的横坐标
# missing_y 指的是缺失的格子的纵坐标
def play_chess(size, chess_board_x, chess_board_y, missing_x, missing_y):
    global step
    # 设立递归的边界
    if size == 1:
        return
    # 追踪的记号
    # trace_step 每次都会为三个位置上的元素填充
    trace_step = step
    step += 1
    size = int(size/2)
    # 左上棋盘处理
    if missing_x - chess_board_x < size and missing_y - chess_board_y < size:
        # 缺失的棋子在处理的范围之内
        play_chess(size, chess_board_x, chess_board_y, missing_x, missing_y)
    else:
        # 缺失的棋子不在处理的范围之内
        chess_board[chess_board_x + size - 1][chess_board_y + size - 1] = trace_step
        play_chess(size, chess_board_x, chess_board_y, chess_board_x + size - 1, chess_board_y + size - 1)

    # 右上棋盘处理
    if missing_x - chess_board_x < size and missing_y - chess_board_y >= size:
        # 缺失的棋子在处理的范围之内
        play_chess(size, chess_board_x, chess_board_y + size, missing_x, missing_y)
    else:
        # 缺失的棋子不在处理的范围之内
        chess_board[chess_board_x + size - 1][chess_board_y + size] = trace_step
        play_chess(size, chess_board_x, chess_board_y + size, chess_board_x + size - 1, chess_board_y + size)

    # 左下棋盘处理
    if missing_x - chess_board_x >= size and missing_y - chess_board_y < size:
        # 缺失的棋子在处理的范围之内
        play_chess(size, chess_board_x + size, chess_board_y, missing_x, missing_y)
    else:
        # 缺失的棋子不在处理的范围之内
        chess_board[chess_board_x + size][chess_board_y + size - 1] = trace_step
        play_chess(size, chess_board_x + size, chess_board_y, chess_board_x + size, chess_board_y + size - 1)

    # 右下棋盘处理
    if missing_x - chess_board_x >= size and missing_y - chess_board_y >= size:
        # 缺失的棋子在处理的范围之内
        play_chess(size, chess_board_x + size, chess_board_y + size, missing_x, missing_y)
    else:
        # 缺失的棋子不在处理的范围之内
        chess_board[chess_board_x + size][chess_board_y + size] = trace_step
        play_chess(size, chess_board_x + size, chess_board_y + size, chess_board_x + size, chess_board_y + size)


play_chess(2**k, 0, 0, missing_point['x'], missing_point['y'])

print_chess_board()
