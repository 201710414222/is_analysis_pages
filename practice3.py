import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
def sushu(n):
    # 判断是否素数
    for i in range(2, n):
        if n % i == 0:  # 判断是否能被整除，返回对应的true和false
            return False
    return True


total = 2
for i in range(3, 1000, 2):
    if sushu(i):#调用素数函数
        total += i#素数进行累加
print(total)
