import matplotlib.pyplot as plt
import jieba
import re
from collections import Counter
from wordcloud import WordCloud
cut_words=""
#读入数据并分词
for line in open('./text1.txt',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
print(all_words)
#统计词出现的次数
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1
print('\n词频统计结果：')
#循环遍历输出
for (k,v) in c.most_common(20):# 输出词频最高的前两个词
    print("%s:%d"%(k,v))
#生成词云图
font = "C:\\Windows\\Fonts\\simsun.ttc"
wc = WordCloud(
    font_path=font,
    background_color='white',
    width=500,
    height=350,
    max_font_size=80,
    min_font_size=10,
    mode='RGB'
)
#产生词云
wc.generate(cut_words[:100])
#保存图片(转换为jpg)

wc.to_file(r"vc.jpg")
#显示结果
plt.figure('New Foucs in USA')
plt.imshow(wc)
plt.axis('off')
plt.show()

