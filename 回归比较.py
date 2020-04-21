import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
# 中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1.读取数据集
datasets_X = []
datasets_Y = []
fr = open('prices.txt','r')
lines = fr.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))
#2.数据加载 
length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length,1])
datasets_Y = np.array(datasets_Y)
#3.数据归一化
minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1])
#4.多项式回归模型
poly_reg = PolynomialFeatures(degree = 2)
poly_reg_3 = PolynomialFeatures(degree = 3)
poly_reg_4 = PolynomialFeatures(degree = 4)
#创建二次,三次，四次多项式特征
X_poly = poly_reg.fit_transform(datasets_X)
X_poly_3 = poly_reg_3.fit_transform(datasets_X)
X_poly_4 = poly_reg_4.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_3 = linear_model.LinearRegression()
lin_reg_4 = linear_model.LinearRegression()
#5.模型拟合/训练
lin_reg_2.fit(X_poly, datasets_Y)
lin_reg_3.fit(X_poly_3, datasets_Y)
lin_reg_4.fit(X_poly_4, datasets_Y)
#构建模型 
linear = linear_model.LinearRegression()
#模型训练
linear.fit(datasets_X, datasets_Y)
# 6.结果可视化
plt.scatter(datasets_X, datasets_Y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.plot(X, lin_reg_3.predict(poly_reg_3.fit_transform(X)), color ='yellow')
plt.plot(X, lin_reg_4.predict(poly_reg_4.fit_transform(X)), color ='black')
plt.plot(X, linear.predict(X), color = 'green')
plt.legend(('线性回归','二阶多项式回归','三阶多项式回归','四阶多项式回归'), loc='upper right')
plt.title('回归分析比较图')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
#7.模型评估
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
# MSE：均方差
y1_pre=linear.predict(datasets_X)
y2_pre=lin_reg_2.predict(X_poly)
y3_pre=lin_reg_3.predict(X_poly_3)
y4_pre=lin_reg_4.predict(X_poly_4)
mse_line= mean_squared_error(datasets_Y, y1_pre)
mse_lin_reg_2= mean_squared_error(datasets_Y, y2_pre)
mse_lin_reg_3= mean_squared_error(datasets_Y, y3_pre)
mse_lin_reg_4= mean_squared_error(datasets_Y, y4_pre)
print("线性回归均方差:",mse_line)
print("二阶多项式回归均方差:",mse_lin_reg_2)
print("三阶多项式回归均方差:",mse_lin_reg_3)
print("四阶多项式回归均方差:",mse_lin_reg_4)
# MAE 平均绝对误差
mae_line = mean_absolute_error(datasets_Y, y1_pre)
mae_lin_reg_2= mean_absolute_error(datasets_Y, y2_pre)
mae_lin_reg_3= mean_absolute_error(datasets_Y, y3_pre)
mae_lin_reg_4= mean_absolute_error(datasets_Y, y4_pre)
print("\n")
print("线性回归平均绝对误差:",mae_line)
print("二阶多项式回归平均绝对误差:",mae_lin_reg_2)
print("三阶多项式回归平均绝对误差:",mae_lin_reg_3)
print("四阶多项式回归平均绝对误差:",mae_lin_reg_4)
