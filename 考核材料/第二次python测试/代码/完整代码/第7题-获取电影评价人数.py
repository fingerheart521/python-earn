"""
任务详情
给定豆瓣票房排行榜，输入指定影片名称 movie_name，如：'熔炉'，输出该电影共多少人进行评价

任务要求
1. 程序接收 str 类型的变量 movie_name，返回 int 类型的变量；
2. 要求去掉数据最后汉字并修改输出数据类型为 int 类型；
3. 票房信息排行榜在下方给出，utf-8编码。

输出示例  输入 "肖申克的救赎"
3013853

网站链接
http://32s465422x.yicp.fun/data/7movietop25/top25.html
"""
import re
import requests
from bs4 import BeautifulSoup


class Solution:
    def doubanTop25(self, movie_name: str) -> int:
        # 获取整个网页
        url = "http://32s465422x.yicp.fun/data/7movietop25/top25.html"
        start = requests.get(url)  # git方法获取网站信息
        start.encoding = "utf-8"  # 设置编码
        all_html = BeautifulSoup(start.text, "lxml")

        # 处理数据，查找符合题目的数据
        movie = all_html.find("span", string=movie_name).parent.parent.parent

        # 查找包含“人评价”的字符串
        pingjia = movie.find("span", string=re.compile(r"人评价")).string[:-3]

        return int(pingjia)


x = Solution
print(x.doubanTop25(0, "肖申克的救赎"))
