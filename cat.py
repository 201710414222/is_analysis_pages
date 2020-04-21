 #-*-coding:GBK -*- 
import numpy as np
import matplotlib.pyplot as plt
import h5py
from lr_utils import load_dataset
train_set_x_orig,train_set_y,test_set_x_orig,test_set_y,classes=load_dataset()

index=2
plt.imshow(train_set_x_orig[index])
plt.show()


print("y="+str(train_set_y[:,index])+",it is a "+classes[np.squeeze(train_set_y[:,index])].decode("utf-8")+" picture")

m_train=train_set_x_orig.shape[1]#训练集的图片数量

m_test=test_set_y.shape[1]#测试集的图片数量

num_px=train_set_x_orig.shape[1]#训练，测试集里面的图片的宽度和高度


print("训练集的数量：m_train="+str(m_train))
print("测试集的数量：m_test="+str(m_test))
print("每张图片的宽/高：num_px="+str(num_px))
print("每张图片的大小:（"+str(num_px)+","+str(num_px)+",3)")
print("训练集_图片的维数:"+str(train_set_x_orig.shape))
print("训练集_标签的维数:"+str(train_set_y.shape))
print("测试集_图片的维数:"+str(test_set_x_orig.shape))
print("测试集_标签的维数:"+str(test_set_y.shape))

#x_flatten=x.reshape(x.shape[0],-1).T  
#将训练集的维度降低并转置。

train_set_x_flatten=train_set_x_orig.reshape(train_set_x_orig.shape[0],-1).T

#将测试集的维度降低并转置。
test_set_x_flatten=test_set_x_orig.reshape(test_set_x_orig.shape[0],-1).T


print("训练集_图片的维数:"+str(train_set_x_flatten.shape))
print("训练集_标签的维数:"+str(train_set_y.shape))
print("测试集_图片的维数:"+str(test_set_x_flatten.shape))
print("测试集_标签的维数:"+str(test_set_y.shape))

train_set_x=train_set_x_flatten/255
test_set_x=test_set_x_flatten/255


def sigmoid(z):
	s=1/(1+np.exp(-z))
	return s
	

def initialize_with_zeros(dim):
	
	w=np.zeros(shape=(dim,1))
	b=0
	
	assert(w.shape==(dim,1))#w的维度是（dim,1）
	assert(isinstance(b,float)or isinstance(b,int))#b的类型是float或者是int
	return (w,b)
	
def propagate(w,b,X,Y):
	'''
	w  权重(num_px*num_px*3,1)
	b  偏差
	X  矩阵类型（num_px*num_px*3,训练数量）
	Y  真正的标签矢量（非猫为0 猫为1），矩阵维度为（1，训练数据数量）
	'''
	
	
	m=X.shape[1]
	
	#正向传播
	A=sigmoid(np.dot(w.T,X)+b)
	
	cost=(-1/m)*np.sum(Y*np.log(A)+(1-Y)*(np.log(1-A)))# 计算成本
	
	#反向传播
	dw=(1/m)*np.dot(X,(A-Y).T)
	
	db=(1/m)*np.sum(A-Y)
	
	#确保数据正确
	assert(dw.shape==w.shape)
	assert(db.dtype==float)
	cost=np.squeeze(cost)
	assert(cost.shape==())
	
	
	#用字典保存单位dw,db
	
	grads={
	         "dw":dw,
	         "db":db
	
	}
	return (grads,cost)
	
	
		
print("++++++++++++测试+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
grads,cost=propagate(w,b,X,Y)
print(str(grads["dw"]))
print(str(grads["db"]))
print(str(cost))


def optimize(w,b,X,Y,num_iterations,learning_rate,print_cost=False):
	"""
    通过梯度下降算法
    
    num_iterations  迭代次数
    learn_rate   学习率
    print_cost   每100步计算损失值
    
    返回
    
    params 包含权重和偏差的字典
    grads  包含权重和偏差相对于成本函数的梯度的字典
    成本  优化期间计算的所有成本列表
    
    
    
	"""
	costs=[]
	
	
	for i in range(num_iterations):
		
		grads,cost=propagate(w,b,X,Y)
		
		dw=grads["dw"]
		db=grads["db"]
		
		w=w-learning_rate*dw
		b=b-learning_rate*db
		#记录成本
		if i%100==0:
			costs.append(cost)
		#打印成本数据
		
		if (print_cost) and (i%100==0):
			print("迭代的次数：%i,误差值：%f"%(i,cost))
			
	params={
	          "w":w,
	          "b":b   }
	grads={
	          "dw":dw,
	          "db":db }
	return (params,grads,costs)          
	
print("++++++++++++测试+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
params, grads, costs=optimize(w,b,X,Y,num_iterations=100,learning_rate=0.009,print_cost=False)
print(str(params["w"]))
print(str(params["b"]))
print(str(grads["dw"]))
print(str(grads["db"]))


def predict(w,b,X):
	"""
	Y_prediction  #包含x中所有图片的所有预测[0 I 1]的一个numpy数组(向量)			
	"""
	m=X.shape[1]	#图片的数量
	Y_prediction=np.zeros((1,m))
	w=w.reshape(X.shape[0],1)
	
	#预测猫在图片中出现的概率
	A=sigmoid(np.dot(w.T,X)+b)
	
	for i in range(A.shape[1]):
		#将概率a[0,i]转化为实际预测p[0,i]
		Y_prediction[0,i]=1 if A[0,i]>0.5 else 0
	#确定
	assert(Y_prediction.shape==(1,m))
	
	return Y_prediction
	
print("++++++++++++测试+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
			
print("predictions="+str(predict(w,b,X)))		
		
def model(X_train,Y_train,X_test,Y_test,num_iterations=2000,learning_rate=0.5,print_cost=False):
	w,b=initialize_with_zeros(X_train.shape[0])
	
	parameters, grads, costs=optimize(w,b,X_train,Y_train,num_iterations,learning_rate,print_cost)
	#从字典中检索w和b
	w,b=parameters["w"],parameters["b"]
	#预测测试/训练集的列子
	Y_prediction_test=predict(w,b,X_test)
	Y_prediction_train=predict(w,b,X_train)
	
	#打印训练后的准确性
	
	print("训练集准确性",format(100-np.mean(np.abs(Y_prediction_train-Y_train))*100),"%")
	print("测试集准确性",format(100-np.mean(np.abs(Y_prediction_test-Y_test))*100),"%")
	
	d={  
	         "costs":costs,
	         "Y_prediction_test":Y_prediction_test,
	          "Y_prediction_train":Y_prediction_train,
	          "w":w,
	          "b":b,
	          "learning_rate":learning_rate,
	          "num_iterations":num_iterations 
	          }                
	return d

print("++++++++++++测试modle+++++++++++")
d=model(train_set_x,train_set_y,test_set_x,test_set_y,num_iterations=10000,learning_rate=0.005,print_cost=True)

#绘图
costs=np.squeeze(d['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations(per hundreds)')
plt.title("learning rate="+str(d["learning_rate"]))
plt.show()
