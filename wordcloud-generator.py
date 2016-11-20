#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
/!\ ONLY WORKS WITH PYTHON < 3 BECAUSE OF THE WORDCLOUD PACKAGE
"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

# IMPORT MASK IMAGE
change_coloring = imread("Icon_c-dot2.png")

# IMPORT WORD LIST AND COUNT
text = pd.read_csv("word_count.csv", names=["words"], encoding='utf-8')
text = [tuple(x) for x in text.to_records()]

# SPECIFY WORDCLOUD PARAMETERS
# Large `max_font_size` gives more weight to the frequencies of the words than their ranking
wordcloud = WordCloud(font_path = "Change Calibre-Bold.otf",
                      background_color="white", mask=change_coloring,
                      scale = 10, random_state=2017, max_font_size=50000)

# GENERATE THE WORDCLOUD
wordcloud.generate_from_frequencies(text)

# PLOT THE WORD CLOUD AND SAVE IT IN HIGH RES
image_colors = ImageColorGenerator(change_coloring)
plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.axis("off")
plt.savefig('final.png', dpi = 1000)
