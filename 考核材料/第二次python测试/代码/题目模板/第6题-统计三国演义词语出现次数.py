"""
任务详情
使用jieba库进行分析，完成下方对《三国演义》中词汇的分析任务
请将右边的函数  sanguoText() 补充完整，使其能够输出单词及其对应的词频。

任务要求
1. 使用 Jieba 库对文本进行分词；
2. 函数 sanguoText() 不接收任何数据；返回一个列表；
3. 只保留词语长度大于等于 2 的词语的词频统计；
4. 最终要求不输出 "\r\n" 的词频，请设法去除；
5. 文本建议使用 requests 库进行读取，UTF-8 编码方式，否则无法正确读取文本。

输出示例  输入 无输入
[('曹操', 939), ('孔明', 831), ...... ('鼎足三分', 1), ('牢骚', 1)]

网站链接
http://32s465422x.yicp.fun/data/6sanguo/sanguoyanyi.txt
"""
import jieba
import requests


class Solution:
    def sanguoText(self) -> list:
        pass


x = Solution()
print(x.sanguoText())
