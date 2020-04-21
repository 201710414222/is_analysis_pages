import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
w=[0,4,5,2,1,6]#物品重量
v=[0,45,57,22,11,67]#物品的价值
n=len(w)-1#物品数

x=[False for raw in range(n+1)]#x[i]为ture表示应该偷走i个物品
#生成动态规划表啊a[i,j]

# 递归产生动态规划表
def knap(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j >= w[i]) and (a[i - 1][j - w[i]] + v[i] > a[i - 1][j]):
                a[i][j] = a[i - 1][j - w[i]] + v[i]
            else:
                a[i][j] = a[i - 1][j]
    # 回溯
    j = m
    for i in range(n, 0, -1):
        if a[i][j] > a[i - 1][j]:
            x[i] = True
            j = j - w[i]
    return a[n][m]
    # 输出程序结果
try:
    m = eval(input())  # 背包容量
    if (m <= 0):
        print('无效输入')
    else:
        a = [[0 for col in range(m + 1)] for raw in range(n + 1)]
        knap(5, m)
        print('所拿物品为：')
    for i in range(1, n + 1):
      if x[i] == True:
        print('物品:', i)
except:
     print('无效输入')
