# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:22:47 2020

@author: USER
"""



import pandas as pd

'''
pd1 = pd.read_csv("C:/Users/USER/Downloads/all20201013_1.csv",encoding='UTF-8')
pd2 = pd.read_csv("C:/Users/USER/Downloads/all20201013_2.csv",encoding='UTF-8')
pd3 = pd.read_csv("C:/Users/USER/Downloads/all20201013_3.csv",encoding='UTF-8')

pd_12 = pd.concat([pd1, pd2], ignore_index=True) # ignore index
pd_123= pd.concat([pd_12,pd3],ignore_index=True)
pd_all = pd_123[pd_123['comment'].notna()] #清除空白


pd_done = pd_all[~pd_all.comment.str.contains("原始評論")] #清除google翻譯
pd_done.to_csv('C:/Users/USER/Downloads/customer_review_unclean.csv',encoding='utf8')
#print(pd_done.head())
'''
import jieba
import numpy as np
import jieba.analyse
import codecs

'''
jieba.set_dictionary('C:/Users/USER/Downloads/dict.txt') #繁中字典

comment = pd.DataFrame(pd_done, columns = ["comment"]).values.tolist()

def isNaN(string):
    return string != string

stopWords=[]
comment_cut=[]
stopWords = [line.strip() for line in codecs.open('C:/Users/USER/Downloads/stopWords.txt', 'r', 'utf-8').readlines()]
#stopWords.append(stopwords)

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
final_test.to_csv('C:/Users/USER/Downloads/cleaned_customer_review.csv',encoding='utf8',index=True)
print("分詞＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿done")

#合併csv
#data_1028 = pd.merge(pd_done,final_test,left_on=None)
#data_1028 = pd_done.merge(final_test,left_index=True,right_index=True)

#data_1028.to_csv('C:/Users/USER/Downloads/20201028.csv',encoding='utf8',index=True)
print("合併＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿done")

'''
data_1028=pd.read_csv('C:/Users/USER/Downloads/20201028.csv',encoding='utf8')
dic = pd.read_csv("C:/Users/USER/Downloads/opinion_word_utf8.csv",encoding='UTF-8')
dic_df = pd.DataFrame(dic)
dic_df.columns = ["詞","機器分數","正面標記數","中立標記數","負面標記數","非意見詞標記數","非詞標記數"]
keyword = dic_df["詞"].values.tolist()
score = dic_df["機器分數"].values.tolist()
sn_score_list = []


final_  = pd.DataFrame(data_1028, columns = ["comment_cut"]).values.tolist()
for c in final_:
    word_count = 0
    sn_score = 0.0;
    for w in str(c).split(" "):
        count = keyword.count(w)
        if count != 0:
            #print(w + ' count: ' + str(count) + ' score: ' + str(score[keyword.index(w)]) + '*' + str(count))
            sn_score += score[keyword.index(w)] * count
            if score[keyword.index(w)] != 0:
                word_count += count
                if word_count !=0:
                    sen_score=round(sn_score/word_count,5)
                else:
                    sen_score=0
    sn_score_list.append(sen_score)
            #print('now sn_score =  ' + str(sn_score))
    print(word_count)
    print('c\ntotal: ' + str(sn_score))
    
print(sn_score_list)

df1 = pd.DataFrame(sn_score_list)
df1.columns = ["s_score"]
df1.to_csv('C:/Users/USER/Downloads/sen_score_customer_1028.csv',encoding='utf8',index=False)

data_1028_sen = pd.concat([data_1028,df1],axis=1)
data_1028_sen.to_csv('C:/Users/USER/Downloads/data_1028.csv',encoding='utf8',index=False)


