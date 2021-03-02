#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:54:11 2020

@author: lee
"""

import jieba
import pandas as pd
import numpy as np
import jieba.analyse
import codecs



jieba.set_dictionary('C:/Users/USER/anaconda3/pkgs/jieba-0.39-pyh9f0ad1d_1/site-packages/jieba/dict.txt') #繁中字典
#jieba.analyse.set_stop_words('/Users/lee/opt/anaconda3/pkgs/jieba-0.39-py_1/site-packages/jieba/stopWords.txt')



pd.set_option('max_colwidth',500) #設置pandas的顯示長度
comment_cut=[] 
data = pd.read_csv('C:/Users/USER/Downloads/data_1015.csv',encoding='UTF-8',dtype=str)
comment = pd.DataFrame(data, columns = ["comment"]).values.tolist()



#print(comment)

def isNaN(string):
    return string != string

stopWords=[]


stopWords = [line.strip() for line in codecs.open('C:/Users/USER/Downloads/stopWords.txt', 'r', 'utf-8').readlines()]
#stopWords.append(stopwords)
print(stopWords)

for c in comment:
    #print(c)
    if isNaN(str(c)) ==True :
        comment_cut.append(c)
    else:
        result_com = jieba.cut(str(c),cut_all=False)
        remainderWords =  filter(lambda a: a not in stopWords and a != '\n' ,result_com)
        comment_cut.append(" ".join(remainderWords))

for qqq in comment_cut:
    print(qqq)
    
final_test = pd.DataFrame(comment_cut)
final_test.columns = ['comment_cut']
final_test.to_csv('C:/Users/USER/Downloads/cleaned_.csv',encoding='utf8',index=True)
print("分詞＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿done")

#合併csv
df1 = pd.read_csv('C:/Users/USER/Downloads/cleaned_.csv')
df2 = pd.read_csv('C:/Users/USER/Downloads/data_1015.csv')

df = df1.merge(df2,left_index=True,right_index=True)
df.to_csv('C:/Users/USER/Downloads/cleaned_1015.csv',encoding='utf8',index=True)
print("合併＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿done")




