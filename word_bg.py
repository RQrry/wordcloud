#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 读取文件
filename = 'src/flipped.txt'
with open(filename) as f:
	mytext = f.read()
bg_pic = np.array(Image.open('img/bg2.jpg'))

# 生成词云
wordcloud = WordCloud(mask=bg_pic, background_color='white').generate(mytext)
# img_colors = ImageColorGenerator(bg_pic)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片
wordcloud.to_file('img/flipped_bg.jpg')