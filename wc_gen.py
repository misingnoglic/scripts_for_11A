#!/usr/bin/env python
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS



def make_wordcloud(corpus, name):
	d = path.join(path.dirname(__file__), "wordclouds")
	
	# Read the whole text.
	text = corpus


	stopwords = set(STOPWORDS)
	stopwords.add("want")

	wc = WordCloud(background_color="white", max_words=2000, stopwords=stopwords, width=1200, height=900)
	# generate word cloud
	wc.generate(text)

	# store to file
	wc.to_file(path.join(d, name))
