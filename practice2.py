import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
n = 0
b = 1  # 假设最后一个猴子拿1个桃子
sum = 0  # 剩余的桃子数
while (n < 5):
    sum = 4 * b
    for n in range(0, 5):
        if (sum % 4 != 0):  # 判断是否能分为4份
            break
        else:
            n += 1
            sum = sum / 4 * 5 + 1  # 上一次拿下所剩下的
    b += 1
print(int(sum))
