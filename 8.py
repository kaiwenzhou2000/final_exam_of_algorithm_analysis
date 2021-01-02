# 题目：结合你在数据结构与算法课程中获取的知识，
# 自行设计一种面向字符串的单个关键字查找算法，
# 假定查找范围为普通的一维数组。
# 要求：与之前我们所学的所有查找算法都不完全相同。
# 使用详细的流程图，完整的伪代码，有注释的源代码，
# 等其中的任意一种描述方法均可

mother_str = 'hello word'  # 模板字符串
son_str = 'or'  # 所要查询的字符串

dict_str = {}  # 索引字典


def plus_one(a):
    for i in range(len(a)):
        a[i] += 1


def compare_arr(a, b):
    """
    比较两个数组，找出相同的
    :param a:   数组1
    :param b:   数组2
    :return:    相同的数组
    """
    temp = []
    for i in a:
        for j in b:
            if i == j:
                temp.append(i)
    return temp


# 创建索引字典
index = 0
for i in mother_str:
    if i in dict_str:
        dict_str[i].append(index)
    else:
        dict_str[i] = []
        dict_str[i].append(index)
    index += 1

# 查询子字符串
head = son_str[0]
if head not in dict_str:
    print('模板字符串中没有' + head)
    exit(-1)
arr = dict_str[head]
plus_one(arr)

for i in son_str[1:]:
    if i not in dict_str:
        print('模板字符串中没有' + i)
        exit(-1)
    if arr:
        arr = compare_arr(arr, dict_str[i])
    else:
        print('查询失败')
        exit(-1)

# 展示结果
for index, content in enumerate(arr):
    print('第' + str(index + 1) + '个匹配项起始于' + str(content - len(son_str) + 1))
