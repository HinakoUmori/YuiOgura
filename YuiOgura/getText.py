# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re

def getText(prmURL, prmCSSSelectorList) :
    url = prmURL
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    ret = []
    for i in prmCSSSelectorList :
        tmpText = str(soup.select(i))
        ret.append(tmpText)

    return ret

# list = ["article.article:nth-child(2) > header:nth-child(1) > h1:nth-child(1) > a:nth-child(1)",
#         "article.article:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1) > img:nth-child(1)"]
# url = "https://lineblog.me/ogurayui/"
# print(getText(url, list))
