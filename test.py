# 初始化图参数 用字典初始初始化这个图
G = {1: {2: 4, 3: 2, 4: 5},
     2: {5: 7, 6: 5},
     3: {6: 9},
     4: {5: 2, 7: 7},
     5: {8: 4},
     6: {10: 6},
     7: {9: 3},
     8: {10: 7},
     9: {10: 8},
     10: {}
     }

inf = 9999
# 保存源点到各点的距离，为了让顶点和下标一致，前面多了一个inf作为哨兵节点。
length = [inf, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf]
Q = []


# FIFO队列实现
def branch(G, v0):
    Q.append(v0)
    dict = G[1]
    while len(Q) != 0:
        # 队列头元素出队
        head = Q[0]
        # 松弛操作，并且满足条件的后代入队
        for key in dict:
            if length[head] + G[head][key] <= length[key]:
                length[key] = length[head] + G[head][key]
                Q.append(key)
        # 松弛完毕，队头出列
        del Q[0]
        if len(Q) != 0:
            dict = G[Q[0]]


branch(G, 1)
print(length[1:])
