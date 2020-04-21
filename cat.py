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

m_train=train_set_x_orig.shape[1]#ѵ������ͼƬ����

m_test=test_set_y.shape[1]#���Լ���ͼƬ����

num_px=train_set_x_orig.shape[1]#ѵ�������Լ������ͼƬ�Ŀ�Ⱥ͸߶�


print("ѵ������������m_train="+str(m_train))
print("���Լ���������m_test="+str(m_test))
print("ÿ��ͼƬ�Ŀ�/�ߣ�num_px="+str(num_px))
print("ÿ��ͼƬ�Ĵ�С:��"+str(num_px)+","+str(num_px)+",3)")
print("ѵ����_ͼƬ��ά��:"+str(train_set_x_orig.shape))
print("ѵ����_��ǩ��ά��:"+str(train_set_y.shape))
print("���Լ�_ͼƬ��ά��:"+str(test_set_x_orig.shape))
print("���Լ�_��ǩ��ά��:"+str(test_set_y.shape))

#x_flatten=x.reshape(x.shape[0],-1).T  
#��ѵ������ά�Ƚ��Ͳ�ת�á�

train_set_x_flatten=train_set_x_orig.reshape(train_set_x_orig.shape[0],-1).T

#�����Լ���ά�Ƚ��Ͳ�ת�á�
test_set_x_flatten=test_set_x_orig.reshape(test_set_x_orig.shape[0],-1).T


print("ѵ����_ͼƬ��ά��:"+str(train_set_x_flatten.shape))
print("ѵ����_��ǩ��ά��:"+str(train_set_y.shape))
print("���Լ�_ͼƬ��ά��:"+str(test_set_x_flatten.shape))
print("���Լ�_��ǩ��ά��:"+str(test_set_y.shape))

train_set_x=train_set_x_flatten/255
test_set_x=test_set_x_flatten/255


def sigmoid(z):
	s=1/(1+np.exp(-z))
	return s
	

def initialize_with_zeros(dim):
	
	w=np.zeros(shape=(dim,1))
	b=0
	
	assert(w.shape==(dim,1))#w��ά���ǣ�dim,1��
	assert(isinstance(b,float)or isinstance(b,int))#b��������float������int
	return (w,b)
	
def propagate(w,b,X,Y):
	'''
	w  Ȩ��(num_px*num_px*3,1)
	b  ƫ��
	X  �������ͣ�num_px*num_px*3,ѵ��������
	Y  �����ı�ǩʸ������èΪ0 èΪ1��������ά��Ϊ��1��ѵ������������
	'''
	
	
	m=X.shape[1]
	
	#���򴫲�
	A=sigmoid(np.dot(w.T,X)+b)
	
	cost=(-1/m)*np.sum(Y*np.log(A)+(1-Y)*(np.log(1-A)))# ����ɱ�
	
	#���򴫲�
	dw=(1/m)*np.dot(X,(A-Y).T)
	
	db=(1/m)*np.sum(A-Y)
	
	#ȷ��������ȷ
	assert(dw.shape==w.shape)
	assert(db.dtype==float)
	cost=np.squeeze(cost)
	assert(cost.shape==())
	
	
	#���ֵ䱣�浥λdw,db
	
	grads={
	         "dw":dw,
	         "db":db
	
	}
	return (grads,cost)
	
	
		
print("++++++++++++����+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
grads,cost=propagate(w,b,X,Y)
print(str(grads["dw"]))
print(str(grads["db"]))
print(str(cost))


def optimize(w,b,X,Y,num_iterations,learning_rate,print_cost=False):
	"""
    ͨ���ݶ��½��㷨
    
    num_iterations  ��������
    learn_rate   ѧϰ��
    print_cost   ÿ100��������ʧֵ
    
    ����
    
    params ����Ȩ�غ�ƫ����ֵ�
    grads  ����Ȩ�غ�ƫ������ڳɱ��������ݶȵ��ֵ�
    �ɱ�  �Ż��ڼ��������гɱ��б�
    
    
    
	"""
	costs=[]
	
	
	for i in range(num_iterations):
		
		grads,cost=propagate(w,b,X,Y)
		
		dw=grads["dw"]
		db=grads["db"]
		
		w=w-learning_rate*dw
		b=b-learning_rate*db
		#��¼�ɱ�
		if i%100==0:
			costs.append(cost)
		#��ӡ�ɱ�����
		
		if (print_cost) and (i%100==0):
			print("�����Ĵ�����%i,���ֵ��%f"%(i,cost))
			
	params={
	          "w":w,
	          "b":b   }
	grads={
	          "dw":dw,
	          "db":db }
	return (params,grads,costs)          
	
print("++++++++++++����+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
params, grads, costs=optimize(w,b,X,Y,num_iterations=100,learning_rate=0.009,print_cost=False)
print(str(params["w"]))
print(str(params["b"]))
print(str(grads["dw"]))
print(str(grads["db"]))


def predict(w,b,X):
	"""
	Y_prediction  #����x������ͼƬ������Ԥ��[0 I 1]��һ��numpy����(����)			
	"""
	m=X.shape[1]	#ͼƬ������
	Y_prediction=np.zeros((1,m))
	w=w.reshape(X.shape[0],1)
	
	#Ԥ��è��ͼƬ�г��ֵĸ���
	A=sigmoid(np.dot(w.T,X)+b)
	
	for i in range(A.shape[1]):
		#������a[0,i]ת��Ϊʵ��Ԥ��p[0,i]
		Y_prediction[0,i]=1 if A[0,i]>0.5 else 0
	#ȷ��
	assert(Y_prediction.shape==(1,m))
	
	return Y_prediction
	
print("++++++++++++����+++++++++++")

w,b,X,Y=np.array([[1],[2]]),2,np.array([[1,2],[3,4]]),np.array([[1,0]])	
			
print("predictions="+str(predict(w,b,X)))		
		
def model(X_train,Y_train,X_test,Y_test,num_iterations=2000,learning_rate=0.5,print_cost=False):
	w,b=initialize_with_zeros(X_train.shape[0])
	
	parameters, grads, costs=optimize(w,b,X_train,Y_train,num_iterations,learning_rate,print_cost)
	#���ֵ��м���w��b
	w,b=parameters["w"],parameters["b"]
	#Ԥ�����/ѵ����������
	Y_prediction_test=predict(w,b,X_test)
	Y_prediction_train=predict(w,b,X_train)
	
	#��ӡѵ�����׼ȷ��
	
	print("ѵ����׼ȷ��",format(100-np.mean(np.abs(Y_prediction_train-Y_train))*100),"%")
	print("���Լ�׼ȷ��",format(100-np.mean(np.abs(Y_prediction_test-Y_test))*100),"%")
	
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

print("++++++++++++����modle+++++++++++")
d=model(train_set_x,train_set_y,test_set_x,test_set_y,num_iterations=10000,learning_rate=0.005,print_cost=True)

#��ͼ
costs=np.squeeze(d['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations(per hundreds)')
plt.title("learning rate="+str(d["learning_rate"]))
plt.show()
