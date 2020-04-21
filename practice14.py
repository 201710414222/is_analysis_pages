
# 1.导入模块
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# 机器学习模型
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
# 机器学习数据集
import sklearn.datasets as datasets
# 绘图
import matplotlib.pyplot as plt

# 2.获取训练数据和预测数据
# 导入 datasets 模块中的数据
digits = datasets.load_digits()
data = digits.data
target = digits.target
images = digits.images
# 划分训练数据
X_train = data[:1600]
Y_train = target[:1600]
# 测试数据
x_test = data[1600:]
y_true = target[1600:]
# 3.确定学习模型
# k 近邻算法模型
knnclf = KNeighborsClassifier(n_neighbors=5)
# logistic 模型
logistic = LogisticRegression(solver='lbfgs')
# 4.用训练数据训练模型
knnclf.fit(X_train, Y_train)
logistic.fit(X_train, Y_train)
# 5.用模型预测结果
y_pre_knn = knnclf.predict(x_test)
y_pre_logistic = logistic.predict(x_test)
# 6.查看算法得分
knn_score = knnclf.score(x_test, y_true)
logistic_score = logistic.score(x_test, y_true)
print(knn_score, logistic_score)

# 7.绘图，展示结果
plt.figure(figsize=(50, 50))
for i in range(50):
    plt.subplot(10, 5, i + 1)
    plt.imshow(x_test[i].reshape(8, 8))
    plt.axis('off')
    title = 'KNN:' + str(y_pre_knn[i]) + '\nLOGIC:' + str(y_pre_logistic[i]) + '\nTrue:' + str(y_true[i])
    plt.title(title)
plt.show()

