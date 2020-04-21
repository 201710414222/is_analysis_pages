import requests
from bs4 import BeautifulSoup
import io
import os
# 获取网页
def geturl(url):
    try:
        r = requests.get(url)
        #查看状态
        r.raise_for_status()
        #设置内容为分析内容
        r.encoding = r.apparent_encoding
        #返回文本内容
        return r.text
    except:
        return "访问失败！"


def getpic(html):
    soup = BeautifulSoup(html, "html.parser")
    #找到父亲节点的class以及标签
    imgs = soup.find('ul', class_='thumbnail-grid').find_all('img')
    print(imgs)
    #遍历输出src
    for img in imgs:
        src = img['src']
        img_url = src

        print(img_url)
        root = "./pic.txt/"
        #以/为分隔符，保留最后一段
        path = root + img_url.split('/')[-1]
        print(path)
        try:
            if not os.path.exists(root):  # 判断是否存在文件并下载img
                os.mkdir(root)
            #如果不存在path，返回图片地址
            if not os.path.exists(path):
                r = requests.get(img_url)
                #打开路径，从写文件内容
                with open(path, "wb")as f:
                    f.write(r.content)
                    f.close()
                    print("文件保存成功！")
            else:
                print("文件已存在！")
        except:
            print("文件爬取失败！")


if __name__ == "__main__":
    html_url = geturl("https://findicons.com/search/nature")
    getpic(html_url)
