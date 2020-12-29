# 题目：设计一个贪心算法（详细的流程图，或者 完整的伪代码，或者 有注释的源代码），
# 把一个真分数表示为埃及分数之和的形式。
# 所谓埃及分数，是指分子为1的分数。如：7/8=1/2+1/3+1/24。

ans = []
num_son: int = 7
num_mother: int = 8


# 辗转相除法，快速求出最大公约数
def gcd(bigger, smaller):
    while bigger % smaller != 0:
        temp = smaller
        smaller = bigger % smaller
        bigger = temp
    return smaller


# 使用暴力贪心算法
def for_loop():
    global num_mother, num_son
    # 暴力贪心算法
    while num_son != 1:
        # 分母从1开始
        i: int = 2
        while num_son / num_mother < 1 / i:
            i += 1
        ans.append(i)
        num_son = num_son * i - num_mother
        num_mother *= i
        g = gcd(num_mother, num_son)
        num_son /= g
        num_mother /= g
    ans.append(int(num_mother))


# 使用推倒公式
def use_math():
    global num_mother, num_son
    flag = True
    while flag or num_son > 1:
        flag = False
        e = int(num_mother / num_son) + 1
        ans.append(e)

        num_son = int(num_son * e) - num_mother
        num_mother = int(num_mother * e)

        g = int(gcd(num_mother, num_son))
        num_son /= g
        num_mother /= g
    ans.append(int(num_mother / num_son))


# for_loop()
use_math()

for i in ans:
    print('1/' + str(i))
