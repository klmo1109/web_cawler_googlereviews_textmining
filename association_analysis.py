# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:57:51 2020

@author: E0090
"""

import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

x = pd.read_csv('C:/Users/E0090/Downloads/pre_data_1018_text.csv')
x= x.dropna()
movieid = x['醫院類別'].tolist()
comment = x['comment_cut'].tolist()

combine = list(zip(movieid,comment))

all_comment = []
store = []
# c=0
for k in range(len(combine)):
    try:
        if movieid[k] == movieid[k+1]:
            store.append(comment[k])
            # c=c+1
            continue
        elif movieid[k] != movieid[k+1] and movieid[k] == movieid[k-1]:
            store.append(comment[k])
            all_comment.append(store)
            store=[]
        elif movieid[k] != movieid[k-1] and movieid[k] != movieid[k+1]:
            store.append(comment[k])
            all_comment.append(store)
            store = []
    except:
        break
        
#print(all_comment)


te = TransactionEncoder()	
df_tf = te.fit(all_comment).transform(all_comment)
	
df = pd.DataFrame(df_tf,columns=te.columns_)




frequent_itemsets = apriori(df,min_support=0.05,use_colnames=True)	
print(frequent_itemsets)
frequent_itemsets.sort_values(by='support',ascending=False,inplace=True)	

association_rule = association_rules(frequent_itemsets,metric='confidence',min_threshold=0.01)	

# association_rule = association_rules(frequent_itemsets, metric="lift", min_threshold=0.01)
print(association_rule)