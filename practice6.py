import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
#用,号隔开输入
ls=input('请输入钱数x,要买的鸡的数目y:').split(",")
#定义钱初始值为0
score=0
#用ls数组获取输入的值
money = int(ls[0])
num =int(ls[1])
#加入判断，因为公鸡和母鸡，鸡喔至少都需要一只，以及在各一只下money的值
if num <3 or money<9:
    print('输入错误，请重新输入')
else:
#特别说明python2版本/表示除法结果为int类型，而python3版本/表示出发，结果有小数点，为flaot类型，要用//表示除法
  for g in range(1,money//5+1):
      #加上钱全部去买母鸡，母鸡最大值为moner//3
    for m in range(1,money//3+1):
        # 加上钱全部去买小鸡，小鸡最大值为3*money
        for x in range(1,3*money+1):
            #统计所花的钱
            score = g*5 + m*3 + float(x)/3
            #判断是否等于钱以及鸡的数量并输出
            if score == money and g+m+x ==num:
                print ('cock=%s,hen=%s,chicken=%s' % (g,m,x))
            else:
                pass
