"""
任务详情
请使用 杭州大牌女装.txt 文本完成提取文本中权重最高的 5 个关键词的任务。

任务要求
1. 程序以数组的形式返回五个关键词，关键词类型是 str；
2. 使用结巴库内置的TextRank 算法抽取关键词，只返回关键词，不必返回权重。关键词的词性必须是名词和动词；
3. 返回的5个关键词至少要有4个关键词与系统内置的答案一致；
4. 返回关键词不需要考虑顺序；
5. 杭州大牌女装.txt使用 requests 库读取，UTF-8编码，链接在下方给出；
6. Jieba库词性表及说明.xlsx 也在下方给出，作为参考。

输出示例  输入 无输入
['裙子', *, *, *, *]

文本链接
http://32s465422x.yicp.fun/data/2&8shop/shop.txt

Jieba库词性表及说明.xlsx链接
http://32s465422x.yicp.fun/data/2&8shop/Jieba%E8%AF%8D%E6%80%A7%E8%A1%A8%E5%8F%8A%E8%AF%B4%E6%98%8E.xlsx
http://3246542v2u.vicp.fun/#s/-WOgl-dQ
"""
import jieba.analyse
import requests


class Solution:
    def itemAnalyse(self) -> list:
        pass


x = Solution
print(x.itemAnalyse(0))
