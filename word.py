#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件
filename = 'src/flipped.txt'
with open(filename) as f:
	mytext = f.read()

# 生成词云
wordcloud = WordCloud(scale=2).generate(mytext)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片
wordcloud.to_file('img/flipped.jpg')