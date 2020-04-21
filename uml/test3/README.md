# 实验三:图书管理领域对象建模
## 1.图书管理系统的类图
### 1.1 类图PlantUML源码如下：
```
@startuml
阅读者信息<|--读者
阅读者信息 :  name:String
阅读者信息 :  ID:String
阅读者信息 :  Sex:char
阅读者信息 :  Max_borrowbook:int
阅读者信息 :  count:int
读者 : ID:String
管理员--|>阅读者信息
管理员 : ID:String
借还书记录"*"--"1"阅读者信息
借还书记录 : 书号:String
借还书记录 : 书名:String
借还书记录 : 作者:String
借还书记录 : 出版社名:String
借还书记录 : 读者姓名:String
借还书记录 : borrowdate:Date
借还书记录 : due_Date:Date
借还书记录 : real_Date:Date
借还书记录 : getDate()
借还书记录 : isOverDate()
借还书记录 : opname()
预约"*"--"1"阅读者信息
预约 : 书名:String
预约 : 作者:String
预约 : 读者ID:String
预约 : 预约时间:Date
Copy_book"*"--"*"预约
Copy_book : 书号:String
Copy_book : 书名:String
Copy_book : 出版号:String
Copy_book : 作者:String
Copy_book : 出版社名:String
Copy_book : count:int
Copy_book"1"--"1"借还书记录
Copy_book"*"--"1"book
book : 书号:String
book : 书名:String
book : 出版号:String
book : 出版社名:String
book : 作者:String
@enduml
```
### 1.2类图如下:
![](.README_images/2.png)
### 1.3类图说明:
（1）管理员类：类名：管理员<<子类>> 属性名：1.1、private： ID<<阅读者证件号>> 1.2、方法：未定。<br/>
（2）读者类：类名：读者<<子类>>；属性名：1.1private：ID<<阅读者证件号>> 1.2、方法：未定<br/>
（3）阅读者信息类:类名：阅读者信息<<父类>>；属性名：1.1private： ID<<阅读者证件号>> 1.2方法：未定。<br/>
（4）借还书记录类(关联类)：类名：借还书记录； 1.1、属性名：1.2、private： 书号<<图书编号>> 类型：String； 1.3、private： 书名<<图书名>> 类型：String； 1.4、private：读者姓名<<>> 类型：String； 1.5、private： 出版社名<<图书出版社名>> 类型：String； 1.6private： 作者<<图书作者姓名>> 类型：String； 1.7、private：borrowdate<<所借图书日期>> 类型：Date； 1.8、private：due_Date<<图书应还日期>> 类型：Date； 1.9、private：real_Date<<图书实还日期>> 类型：Date； 2.0、方法： 2.1、private：getDate（） 返回值：Date； 2.2、private：isOverDate（） 返回值：bool； 2.3、private：opname（） 返回值：void；<br/>
（5）预约类：1.1、属性：1.2：private：书名<<预约书名>> 类型：String；1.3：private：作者<<图书作者>> 类型：String； 1.4：private：读者ID<<预约者ID>> 类型：String； 1.5：private：预约时间<<预约时间>> 类型：Date；1.6、方法：未定。<br/>
（6）备份书籍类（copy_book）：类名：copy_book； 1.1、属性名：1.2、private： 书号<<图书编号>> 类型：String； 1.3、private： 书名<<图书名>> 类型：String； 1.4、private： 出版号<<图书出版编号>> 类型：String； 1.5、private： 出版社名<<图书出版社名>> 类型：String； 1.6、private： 作者<<图书作者姓名>> 类型：String； 1.7、private：count<<图书数量>> 类型：String； 1.8、方法：未定。<br/>
（7）书类（book）：属性名：1.1、private： 书号<<图书编号>> 类型：String； 1.2、private： 书名<<图书名>> 类型：String； 1.3、private： 出版号<<图书出版编号>> 类型：String； 1.4、private： 出版社名<<图书出版社名>> 类型：String； 1.5、private： 作者<<图书作者姓名>> 类型：String； 1.6、方法：未定。<br/>
## 2.图书管理系统的对象图:
### 2.1类管理员的对象图:
#### 源码如下:
```
@startuml
object 管理员 {
ID = 123456
}
@enduml
```
### 对象图如下:
![](.README_images/7b80aa69.png)
### 2.2类读者的对象图:
#### 源码如下:
```
@startuml
object 读者 {
ID = 234567
}
@enduml
```
#### 对象图如下:
![](.README_images/3f455f3d.png)
### 2.3类book的对象图如下:
#### 源码如下:
```
@startuml
object book{
书号="5"
书名="《孔子》"
出版社号="3456"
出版社名="清华大学出版社"
作者="fd"
}
@enduml
```
#### 对象图如下:
![](.README_images/9cdd3e91.png)
