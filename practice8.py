import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
values = [50, 20, 10, 5, 1]
counts = [4, 3, 1, 10, 80]
result = [0, 0, 0, 0, 0]


def change(pay):
    for i in range(len(values)):
        if pay >= values[i]:
            count = pay // values[i]
            result[i] = count
            counts[i] -= count
            pay = pay - count * values[i]
    return result

if __name__ == "__main__":
    try:
        x, y, z = eval(input())
        needcharge = y - z * x
        if needcharge == 0:
            print("不用找零")
        elif needcharge > 0:
            change(needcharge)
            for i in range(len(result)):
                print("%d元:%d\n" % (values[i], result[i]))
        else:
            print("支付金额不足")
    except:
        print("无效输入")
