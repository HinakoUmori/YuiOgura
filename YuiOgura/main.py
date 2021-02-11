import getText
import re
import sys
sys.path.append('../')
from tweet import tweet
import time

url = "https://lineblog.me/ogurayui/"
keyList = ["article.article:nth-child(2) > header:nth-child(1) > h1:nth-child(1) > a:nth-child(1)"]

CK = '***'
CS = '***'
AT = '***'
AS = '***'

while True :
    text = getText.getText(url, keyList)
    str_text = str(text[0])
    str_text = re.sub('<.*?>', '', str_text)
    # str_text.replace('白', '')
    str_text = str_text.replace('[', '')
    str_text = str_text.replace(']', '')
    # print(str_text)
    textList = []
    textList.append(str_text)

    f = open('title.txt', 'r')
    data = f.read()
    f.close()

    if data != textList[0] :
        # tweet(CK, CS, AT, AS, textList)
        f = open('title.txt', 'w')
        f.write(textList[0])
        f.close()
        print(textList[0])
    else :
        print('same')
    time.sleep(1)
