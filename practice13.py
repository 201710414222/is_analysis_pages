def dregree4():
    # 多项式回归模型
    poly_reg = PolynomialFeatures(degree=4)
    # 创建三次多项式特征
    X_poly = poly_reg.fit_transform(datasets_X)
    lin_reg_4 = linear_model.LinearRegression()
    # 模型拟合/训练
    lin_reg_4.fit(X_poly, datasets_Y)
    # MSE：均方差
    y4_pre = lin_reg_4.predict(X_poly)
    mse_lin_reg_2 = mean_squared_error(datasets_Y, y4_pre)
    print("四项式回归均方差:", mse_lin_reg_2)
    # MAE 平均绝对误差
    mae_lin_reg_4 = mean_absolute_error(datasets_Y, y4_pre)
    print("四项式回归平均绝对误差:", mae_lin_reg_4)
    # 图像中显示
    plt.scatter(datasets_X, datasets_Y, color='red')
    plt.plot(X, lin_reg_4.predict(poly_reg.fit_transform(X)), color='blue')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.title('四阶模型图')
    plt.show()
def dregree3():
    # 多项式回归模型
    poly_reg = PolynomialFeatures(degree=3)
    # 创建三次多项式特征
    X_poly = poly_reg.fit_transform(datasets_X)
    lin_reg_3 = linear_model.LinearRegression()
    # 模型拟合/训练
    lin_reg_3.fit(X_poly, datasets_Y)
    # MSE：均方差
    y3_pre = lin_reg_3.predict(X_poly)
    mse_lin_reg_3 = mean_squared_error(datasets_Y, y3_pre)
    print("三项式回归均方差:", mse_lin_reg_3)
    # MAE 平均绝对误差
    mae_lin_reg_3 = mean_absolute_error(datasets_Y, y3_pre)
    print("三项式回归平均绝对误差:", mae_lin_reg_3)
    # 图像中显示
    plt.scatter(datasets_X, datasets_Y, color='red')
    plt.plot(X, lin_reg_3.predict(poly_reg.fit_transform(X)), color='blue')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.title('三阶模型图')
    plt.show()
def dregree2():
    # 多项式回归模型
    poly_reg = PolynomialFeatures(degree=2)
    # 创建二次多项式特征
    X_poly = poly_reg.fit_transform(datasets_X)
    lin_reg_2 = linear_model.LinearRegression()
    # 模型拟合/训练
    lin_reg_2.fit(X_poly, datasets_Y)
    # MSE：均方差
    y2_pre = lin_reg_2.predict(X_poly)
    mse_lin_reg_2 = mean_squared_error(datasets_Y, y2_pre)
    print("二项式回归均方差:", mse_lin_reg_2)
    # MAE 平均绝对误差
    mae_lin_reg_2 = mean_absolute_error(datasets_Y, y2_pre)
    print("二项式回归平均绝对误差:", mae_lin_reg_2)
    # 图像中显示
    plt.scatter(datasets_X, datasets_Y, color='red')
    plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.title('二阶模型图')
    plt.show()
def LinearRegression():

    # 构建模型
    linear = linear_model.LinearRegression()
    # 模型训练
    linear.fit(datasets_X, datasets_Y)
    # MSE：均方差
    y1_pre = linear.predict(datasets_X)
    mse_line = mean_squared_error(datasets_Y, y1_pre)
    print("线性回归均方差:", mse_line)
    # MAE 平均绝对误差
    mae_line = mean_absolute_error(datasets_Y, y1_pre)
    print("线性回归平均绝对误差:", mae_line)
    # 模型可视化
    plt.scatter(datasets_X, datasets_Y, color='red')
    plt.plot(X, linear.predict(X), color='blue')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.title('线性回归模型图')
    plt.show()
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import linear_model
    from sklearn.preprocessing import PolynomialFeatures
    # 7.模型评估
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import mean_absolute_error
    # 中文设置
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 读取数据集
    datasets_X = []
    datasets_Y = []
    fr = open('prices.txt', 'r')
    lines = fr.readlines()
    for line in lines:
        items = line.strip().split(',')
        datasets_X.append(int(items[0]))
        datasets_Y.append(int(items[1]))
    # 数据加载
    length = len(datasets_X)
    datasets_X = np.array(datasets_X).reshape([length, 1])
    datasets_Y = np.array(datasets_Y)
    # 数据归一化
    minX = min(datasets_X)
    maxX = max(datasets_X)
    X = np.arange(minX, maxX).reshape([-1, 1])
    # 构建模型
    linear = linear_model.LinearRegression()
    # 输出线性回归模型
    print(LinearRegression())
    # 输出二阶多项式
    print(dregree2())
    # 输出三阶多项式
    print(dregree3())
    # 输出四阶多项式
    print(dregree4())


