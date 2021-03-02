# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:07:27 2020

@author: E0090
"""

import pandas as pd
import matplotlib.pyplot as plt
import jieba
from jieba import analyse


import codecs
from wordcloud import WordCloud

font = 'C:/Users/USER/anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/TaipeiSansTCBeta-Bold.ttf'
up_dis = pd.read_csv("C:/Users/USER/Downloads/1024/3.4上(含)_地區.csv",encoding='UTF-8',index_col=0)
down_dis= pd.read_csv("C:/Users/USER/Downloads/1024/3.4 下_地區.csv",encoding='UTF-8',index_col=0)
up_reg =  pd.read_csv("C:/Users/USER/Downloads/1024/3.4上(含)_區域.csv",encoding='UTF-8',index_col=0)
down_reg = pd.read_csv("C:/Users/USER/Downloads/1024/3.4 下_區域.csv",encoding='UTF-8',index_col=0)
up_all =  pd.read_csv("C:/Users/USER/Downloads/1024/3.4上(含).csv",encoding='UTF-8',index_col=0)
down_all= pd.read_csv("C:/Users/USER/Downloads/1024/3.4 下.csv",encoding='UTF-8',index_col=0)
data = [up_dis,down_dis,up_reg,down_reg,up_all,down_all]


#print(comment)



'''
loc = data.groupby("分區")
tp = loc.get_group("台北")
n_tw = loc.get_group("北區")
m_tw = loc.get_group("中區")
s_tw = loc.get_group("南區")
p = loc.get_group("南屏")
e_tw =loc.get_group("東區")
tw = [tp,n_tw,m_tw,s_tw,p,e_tw]

loc = data.groupby("醫院類別")
Reg =loc.get_group("區域醫院")
Dis = loc.get_group("地區醫院")
dif = [Reg, Dis]
'''

comment = str(down_all)
word = []
count = []
for x, w in jieba.analyse.extract_tags(comment,topK=50,allowPOS=("ns",'n','vn','v','a','ad','an','d'),withWeight=True):   
    if x != " ":
        word.append(x)
        count.append(w)
zip_two = zip(word,count)
list1= dict(zip_two) 
#= pd.DataFrame(
 #       {'字': word,
  #       '頻率': count,
   #      }).drop([0,1])
if "..." in list1:
    del list1["..."]
print(list1)
word_result = pd.DataFrame([list1])
word_result.column = ["word","tfidf"]
word_result.to_csv('C:/Users/USER/Downloads/down_all.csv',encoding='utf8',index=False)


my_wordcloud = WordCloud(background_color='white',font_path=font,prefer_horizontal=1 ).generate_from_frequencies(list1)
plt.imshow(my_wordcloud)
plt.axis("off")

plt.savefig('C:/Users/USER/Downloads/down_all.png')



#a = jieba.analyse.extract_tags(e_tw, topK=10, withWeight=False, allowPOS=())



def tfide(a):
    word = []
    count = []
    com = str(a)
    for x, w in jieba.analyse.extract_tags(com,topK=50,allowPOS=("ns",'n','vn','v','a','ad','an','d'),withWeight=True):   
        if x != " ":
            word.append(x)
            count.append(w)
    zip_two = zip(word,count)
    list1= dict(zip_two) 
    #= pd.DataFrame(
     #       {'字': word,
      #       '頻率': count,
       #      }).drop([0,1])
    if "..." in list1:
        del list1["..."]
    print(list1)
    word_result = pd.DataFrame([list1])
    word_result.column = ["word","tfidf"]
    word_result.to_csv(str(a)+'.csv',encoding='utf8',index=False)


    my_wordcloud = WordCloud(background_color='white',font_path=font).generate_from_frequencies(list1)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.savefig(str(a)+'.png')


#for y in data:
    #tfide(y)

    


