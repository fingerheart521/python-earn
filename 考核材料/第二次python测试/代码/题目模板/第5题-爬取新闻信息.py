"""
任务详情
给定学校官网新闻页面，按要求完成任务

任务要求
1. 程序无输入。输出为 list 类型
2. 输出格式为['新闻名称, 发布时间, 新闻链接','新闻名称, 发布时间, 新闻链接']
3. 新闻链接为不完整格式，请在前面添加 http://other.zzkjxy.edu.cn 使其正常访问
4. 程序要求将该页面一共15个新闻标题及其信息爬取完成并返回

输出示例  输入 无输入
['信息工程学院召开教研室主任工作例会, 2024-04-22, http://other.zzkjxy.edu.cn/xxgc/list_11/2317.html' ......

网站链接
http://32s465422x.yicp.fun/data/5news/zknews.html
"""
import bs4
import requests


class Solution:
    def zknews(self) -> list:
        pass


x = Solution
print(x.zknews(0))
