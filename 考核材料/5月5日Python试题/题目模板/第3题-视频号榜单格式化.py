"""
任务详情
给定榜单中任意视频号名称，完成以下任务

任务要求
1. 函数接收 str 数据类型的微信视频号名称 videoname；
2. 函数返回为 list 数据类型；
3. 输出 list 中包含 预估粉丝数，日作品数，平均点赞，平均转发，平均转发，平均收藏，有望指数
4. 其中 预估粉丝数 要求将“w+”去掉，并将原数乘10000，输出为 int 数据类型
5. 平均转发 要求将“w+”、“w”去掉，并将带“w”的数据乘10000，注意不带“w”的数据不要乘，输出为 int 数据类型
6. 其他数据保持网页原样，输出为 str 数据类型

输出示例  输入 "央视新闻"
[16610000, '211个', '2.05w', 33000, '181', '2.15w', '1508.55']

网页链接
http://32s465422x.yicp.fun/data/3video_data/video_data.html
"""
import requests
from bs4 import BeautifulSoup


class Solution:
    def videoData(self, videoname: str) -> list:
        pass


x = Solution
print(x.videoData(0, "央视新闻"))
