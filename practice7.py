import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
num=eval(input())
f=[-1]*1001
f[0]=0
f[1]=1
f[2]=2
f[3]=4
#分析：
#f(0)=0,f(1)=1,f(2)=2,f(3)=4,f(4)=7,f(5)=14,可以得到f(x)=f(x-1)+f(x-2)+f（x-3）递推公式
def steps(x):
    #当输入步数为0时，输出为0
    if x<0:
        return  0
    #当输入步数小于4时输出为上面的值
    if x<4:
        return  f[x]
    #当输出为4-1000时，采用递推公式输出
    if 4<=x and x<1000:
        f[x]=steps(x-1)+steps(x-2)+steps(x-3)
        return f[x]
print('跳法数:',end='')
print(steps(num))