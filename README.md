# wordcloud

### 安装

推荐下载[Anaconda](https://www.anaconda.com/download/)，里面集成了大量python库

macOS或者Linux系统安装词云包
```
pip install wordcloud
```
windows系统安装[wordcloud](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)

首先下载和python环境相匹配的wordcloud包，其中36为python3.6，安装
```
pip install wordcloud‑1.4.1‑cp36‑cp36m‑win32.whl
```
### 英文词云

在维基百科中搜索Flipped的电影简介，保存在`flipped.txt`文件中

python代码
```
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
```
![flipped](https://github.com/RQrry/wordcloud/blob/master/img/flipped.jpg)

### 中文词云

英文单词之间采用空格作为强制分隔符，中文的文本就没有这种空格区隔，因此需要对中文进行分词

安装分词包
```
pip install jieba
```
下载中文字体[simsun.ttf](https://link.jianshu.com/?t=https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fnotion-static%2Fb869cb0c7f4e4c909a069eaebbd2b7ad%2Fsimsun.ttf)

将flipped的中文电影介绍保存在`flipped_cn.txt`中

python代码
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件
filename = 'src/flipped_cn.txt'
with open(filename) as f:
	mytext = f.read()

# 生成词云
mytext = ' '.join(jieba.cut(mytext))
wordcloud = WordCloud(font_path='src/simsun.ttf', scale=2).generate(mytext)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片
wordcloud.to_file('img/flipped_cn.jpg')
```
![flipped_cn](https://github.com/RQrry/wordcloud/blob/master/img/flipped_cn.jpg)

### 改变词云的背景

python代码
```
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
```
![flippen_bg](https://github.com/RQrry/wordcloud/blob/master/img/flipped_bg.jpg)
