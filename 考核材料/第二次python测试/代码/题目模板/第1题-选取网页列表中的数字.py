"""
任务详情
给定一个由表格构成的网页，返回指定位置中的数字，数字类型要转换为 int 类型。
后台给出指定位置，位置由行（row）和列（col）构成，如 row = 2, col = 1, 表示第二行第一列，对应的数字是 249；
程序返回的数字必须是 int 类型，类型不正确将导致结果不正确；
后台给出的所有的位置都在表格中，无需考虑边界情况；
表格的第一行是列名，由 A-Z 构成，共 26 列；第一列是行索引，由 1-30 构成，共 30 行。

任务要求
程序给出 int 类型的参数 row 和 col；
程序返回参数是 int 类型。

输出示例  输入 row=29, col=20
252

网站链接
http://32s465422x.yicp.fun/data/1sheet/sheet.html
"""
import requests
from bs4 import BeautifulSoup


class Solution:

    def table_num(self, row: int, col: int) -> int:
        pass


x = Solution()
print(x.table_num(row=29, col=20))
