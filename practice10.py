from matplotlib import pyplot as plt
import csv
import matplotlib
import pandas
import matplotlib.ticker as ticker

# 中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取pollution.csv
filePath = 'pollution.csv'
data = pandas.read_csv(filePath)
# 数据整理
periode = pandas.PeriodIndex(year=data["year"], month=data["month"], day=data["day"], hour=data["hour"], freq="H")
data["datatime"] = periode
# 设置时间为索引
data.set_index("datatime", inplace=True)


# 绘制柱状图
def zhuzhuangtu():
    dataPm25 = data["pm2.5"].dropna()
    dataPm25 = dataPm25.resample("1Y").mean()

    dataTemp = data["TEMP"].dropna()
    dataTemp = dataTemp.resample("1Y").mean()
    datalr = data["Ir"].dropna()
    datalr = datalr.resample("1Y").mean()
    # 显示数据
    plt.figure("PM2.5指数，气压,气温，累计降雨")
    yearList = list(data["year"].drop_duplicates())
    pm25_x = dataPm25.index
    pm25_y = list(dataPm25)
    temp_x = list(dataTemp.index)
    temp_y = list(dataTemp)
    rain_x = list(datalr.index)
    rain_y = list(datalr)
    # 显示
    def autolabel(rects1):
        i = 0
        for rect1 in rects1:
            i += 1
            height = rect1.get_height()
            plt.text(rect1.get_x() + rect1.get_width() / 2. - 0.1, 1.01 * height, '%.3f' % height)
    x = list(range(len(pm25_x)))
    total_width, n = 0.5, 2
    width = total_width / n

    pm25_z = plt.bar(x, pm25_y, width=width, label=u'每年的日平均PM2.5指数', fc='r')
    for i in range(len(x)):
        x[i] += width

    temp_z = plt.bar(x, temp_y, width=width, label=u'每年的日平均气温', tick_label=yearList, fc='b')
    for i in range(len(x)):
        x[i] += width

    rain_z = plt.bar(x, rain_y, width=width, label=u'每年的日平均降雨', tick_label=yearList, fc='g')
    plt.legend()
    plt.xlabel("年份", fontsize=10)
    plt.ylabel("数量", fontsize=10)
    autolabel(pm25_z)
    autolabel(temp_z)
    autolabel(rain_z)
    plt.show()


# 绘制子图
def zitu():
    # 显示数据
    plt.figure("PM2.5指数，气温，,气压，累计降雨")
    dataPm251 = data["pm2.5"].dropna()
    dataPm251 = dataPm251.resample("1M").mean()
    dataTemp1 = data["TEMP"].dropna()
    dataTemp1 = dataTemp1.resample("1M").mean()
    dataPress1 = data["PRES"].dropna()
    dataPress1 = dataPress1.resample("1M").mean()
    dataIr1 = data["Ir"].dropna()
    dataIr1 = dataIr1.resample("1M").mean()
    pm25_x1 = list(dataPm251.index.strftime("%Y-%m"))
    pm25_y1 = list(dataPm251)
    temp_x1 = list(dataTemp1.index.strftime("%Y-%m"))
    temp_y1 = list(dataTemp1)
    press_x1 = list(dataPress1.index.strftime("%Y-%m"))
    press_y1 = list(dataPress1)

    rain_x1 = list(dataIr1.index.strftime("%Y-%m"))
    rain_y1 = list(dataIr1)
    # 绘制第一个子图
    ax = plt.subplot(221)
    pm25_z1 = plt.plot(pm25_x1, pm25_y1, ls="-", linewidth=2, color='red', marker='*')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.title("pm2.5趋势图")
    plt.ylabel("pm2.5数值", fontsize=10)
    # 绘制第二个子图
    ax = plt.subplot(222)
    temp_z1 = plt.plot(temp_x1, temp_y1, ls="-", linewidth=2, color='black', marker='*')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.title("气温趋势图")
    plt.ylabel("气温数值", fontsize=10)
    # 绘制第三个子图
    ax = plt.subplot(223)
    temp_z1 = plt.plot(press_x1, press_y1, ls="-", linewidth=2, color='green', marker='*')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.title("气压趋势图")
    plt.ylabel("气压数值", fontsize=10)
    # 绘制第四个子图
    ax = plt.subplot(224)
    rain_z1 = plt.plot(rain_x1, rain_y1, ls="-", linewidth=2, marker='*')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.title("降雨量趋势图")
    plt.ylabel("降雨数值", fontsize=10)
    plt.show()
# 绘制折线图
def zhexiantu():
    yearList = list(data["year"].drop_duplicates())
    pm25Max5Month = []
    dataPm25 = data["pm2.5"].resample("1M").mean()
    dayList = []
    for year in yearList:
        tmpPm25Max5Month = []
        tmpDayList = []
        for month in dataPm25[str(year)].nlargest(5).sort_index().index.month:
            tmp = data["pm2.5"][str(year) + '-' + str(month)].resample("1D").mean()

            tmpPm25Max5Month += (list(tmp.values))
        pm25Max5Month.append(tmpPm25Max5Month)

        for i in range(len(tmpPm25Max5Month)):
            tmpDayList.append(i + 1)
        dayList.append(tmpDayList)
    label = [u'2010年', u'2011年', u'2012年', u'2013年', u'2014年']

    colors = [
        'black',
        'blue',
        'green',
        'yellow',
        'navy',
        'pink'
    ]
    fig, ax = plt.subplots()
    ax.set_title("每年PM2.5指数平均值最高的5个月，获取每天的PM2.5指数")
    for i in range(len(dayList)):
        ax.plot(dayList[i], pm25Max5Month[i], color=colors[i], linewidth=1.0, label=label[i], linestyle='-')
        ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
    plt.xlabel("天数", fontsize=10)
    plt.ylabel("pm2.5平均值", fontsize=10)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # 输出柱状图
    print(zhuzhuangtu())
    # 输出4个子图
    print(zitu())
    # 输出折现图
    print(zhexiantu())



