"""
任务详情
采用Python自带的函数库进行数据操作，完成任务下方《爱丽丝梦游仙境》英文文本词频的分析。
请将右边的函数  aliceText() 补充完整，使其能够输出某个单词的词频。

任务要求
1. 不得直接使用 Jieba 库对文本进行分词；
2. 函数 aliceText() 接收一个英文单词 word，str 数据类型；返回该单词的词频，int 数据类型；
3. 只保留单词长度大于等于 3 的单词的词频统计；
4. 英文单词不区分大小写；
5. 不同时态和单复数的英文单词为不同英文单词，不需要合并词频统计。如果文本中没有该单词，词频为0；
6. 文本可以使用 requests 库进行读取，UTF-8 编码方式，否则无法正确读取文本。

输出示例  输入 "Pictures"
3

网页链接
http://32s465422x.yicp.fun/data/4alice/alice.txt
"""
import re
import requests


class Solution:
    def aliceText(self, word: str) -> int:
        num = 0
        word = word.lower()

        url = "http://32s465422x.yicp.fun/data/4alice/alice.txt"
        start = requests.get(url)
        start.encoding = "utf-8"
        txt = start.text
        txt = re.sub("[\W]", " ", txt)
        txt = txt.lower()
        txt = re.findall("[\w]{3,}", txt)

        for i in txt:
            if word == i:
                num += 1
            else:
                continue

        return num


x = Solution
print(x.aliceText(0, "Pictures"))
