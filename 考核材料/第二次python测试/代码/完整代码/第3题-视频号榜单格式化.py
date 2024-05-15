"""
任务详情
给定榜单中任意视频号名称，完成以下任务

任务要求
1. 函数接收 str 数据类型的微信视频号名称 videoname；
2. 函数返回为 list 数据类型；
3. 输出 list 中包含 预估粉丝数，日作品数，平均点赞，平均转发，平均转发，平均收藏，有望指数
4. 其中 预估粉丝数 要求将“w+”去掉，并将原数乘10000，输出为 int 数据类型
5. 日作品数最后加上单位“个”
6. 平均转发 要求将“w+”、“w”去掉，并将带“w”的数据乘10000，注意不带“w”的数据不要乘，输出为 int 数据类型
7. 其他数据保持网页原样，输出为 str 数据类型

输出示例  输入 "央视新闻"
[16610000, '211个', '2.05w', 33000, '181', '2.15w', '1508.55']

网页链接
http://32s465422x.yicp.fun/data/3video_data/video_data.html
"""
import requests
from bs4 import BeautifulSoup


class Solution:
    def videoData(self, videoname: str) -> list:
        url = "http://32s465422x.yicp.fun/data/3video_data/video_data.html"
        start = requests.get(url)  # git方法获取网站信息
        start.encoding = "utf-8"  # 设置编码
        all_html = BeautifulSoup(start.text, "lxml")

        videoname_html = all_html.find("p", string=videoname).parent.parent.parent.parent.find_all("div")

        fen_si = int(videoname_html[4].string[:-2]) * 10000
        ri_zuo_pin = videoname_html[5].string + "个"
        dian_zan = videoname_html[6].string
        zhuan_fa = videoname_html[7].string
        if "w+" in zhuan_fa:
            zhuan_fa = int(float(zhuan_fa.replace("w+", "")) * 10000)
        elif "w" in zhuan_fa:
            zhuan_fa = int(float(zhuan_fa.replace("w", "")) * 10000)
        else:
            zhuan_fa = int(zhuan_fa)
        shou_cang = videoname_html[8].string
        ping_lun = videoname_html[9].string
        zhi_shu = videoname_html[10].string

        return [fen_si, ri_zuo_pin, dian_zan, zhuan_fa, shou_cang, ping_lun, zhi_shu]


x = Solution
print(x.videoData(0, "央视新闻"))
