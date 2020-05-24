# 基于GitHub的实验管理平台的分析与设计
##1.概述：
- 基于GitHub的实验管理平台的作用是在线管理实验成绩的Web应用系统。学生和老师的实验内容均存放在GitHUB 页面上。
- 学生的功能主要有：一是设置自己的GitHub用户名，二是查询自己的实验成绩。学生的GitHub用户名是公开的，但成绩不公开。
- 老师的功能主要有：一是批改每个学生的成绩，二是查看每个学生的成绩。
- 老师和学生都能通过本系统的链接方便地跳转到学生的每个GitHUB实验目录，以便批改实验或者查看实验情况。
- 实验成绩按数字分数计算，每项实验的满分为100分，最低为0分。
- 系统自动计算每个学生的所有实验的平均分。
##2.系统总体架构：
![](.README_images/1.png)
界面设计参见：https://201710414222.github.io/is_analysis_pages/ui1/index.html
##3.用例图设计：([源码](1.puml))
![](.README_images/2.png)
##4.类图设计：([源码](2.puml))
![](.README_images/3.png)
##5.数据库设计：
[参见数据库设计](数据库设计.md)