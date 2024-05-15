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
        pass


x = Solution
print(x.doubanTop25(0, "肖申克的救赎"))
