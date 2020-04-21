import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
aqi = eval(input('\n'))#aqi为输入值
if aqi <= 0 or aqi > 500:
    print('无效数据，请重新输入！')
elif aqi <= 35:
    print('优')
elif aqi <= 75:
    print('良')
elif aqi <= 115:
    print('轻度污染')
elif aqi <= 150:
    print('中度污染')
elif aqi <= 250:
    print('重度污染')
elif aqi <= 500:
    print('严重污染')
