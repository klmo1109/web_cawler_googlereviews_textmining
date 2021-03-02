#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:42:55 2020

@author: lee
"""

from selenium import webdriver
import time
import pandas as pd

userreview = []
               
#hos_list = [h1,h2,h3,h4,h5,h6,h7,h8,h9]
h3 = "https://www.google.com/search?q=%E4%BA%9E%E6%B4%B2%E5%A4%A7%E5%AD%B8%E9%99%84&oq=%E4%BA%9E%E6%B4%B2%E5%A4%A7%E5%AD%B8%E9%99%84&aqs=chrome..69i57j0l7.179j0j9&sourceid=chrome&ie=UTF-8#lrd=0x34693b153b3bc8c3:0xbf4d516364314484,1,,,"
h4 = "https://www.google.com/search?q=%E5%93%A1%E6%A6%AE%E9%86%AB%E9%99%A2&oq=%E5%93%A1%E6%A6%AE%E9%86%AB%E9%99%A2&aqs=chrome..69i57j0l7.262j0j9&sourceid=chrome&ie=UTF-8&npsic=0&rflfq=1&rlha=0&rllag=24351935,121166211,74456&tbm=lcl&rldimm=17550056024149961087&lqi=Cgzlk6Hmpq7phqvpmaJaIAoO5ZOhIOamriDphqvpmaIiDuWToSDmpq4g6Yar6Zmi&ved=2ahUKEwj0np738bHsAhUcyIsBHQ4KDtQQvS4wAnoECAwQMw&rldoc=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rlst=f#lrd=0x346936f5776fb019:0xf38e52f843a9a97f,1,,,&rlfi=hd:;si:17550056024149961087,l,Cgzlk6Hmpq7phqvpmaJaIAoO5ZOhIOamriDphqvpmaIiDuWToSDmpq4g6Yar6Zmi;mv:%5B%5B25.192543399999998,121.82912469999998%5D,%5B23.883170399999997,120.49489439999999%5D%5D;tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
hos_lists = [h3,h4] #測試

all_hos = pd.read_csv("C:/Users/USER/Downloads/all_hos_name_20201013 - 工作表5.csv",encoding='UTF-8')
all_hos_web = pd.DataFrame(all_hos, columns = ["hos_web"]).values.tolist()
#all_hos_str =  ' '.join([str(a) for a in all_hos_web])
#all_com = all_hos_str.split("['")[1].split("']")[0]

#print(all_list)
#print(all_hos_web)


for ro in all_hos_web:
    r = "".join(ro)
    #driver設置
    #reviews = driver.find_elements_by_css_selector('.gws-localreviews__google-review');
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(r)#ro.split("['")[1].split("']")[0])
    driver.implicitly_wait(5) #本來是20
    name = driver.find_element_by_css_selector('.P5Bobd').text;
    #print ("now in "+ name+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #driver.quit() ######等下刪掉

    
    
    name = driver.find_element_by_css_selector('.P5Bobd').text;
    hh_score = driver.find_element_by_css_selector('.review-score-container >div > g-review-stars > span').get_attribute('aria-label');
    h_score = hh_score.split('評等：')[1].split(' (最高：5)')[0];
    comment_list = []

    print ("now in "+ name+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
    
    for i in range(1,100): #觸發滾輪
        time.sleep(1)
        #driver.implicitly_wait(5)
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', driver.find_element_by_css_selector('.review-dialog-list'))
    
    #allReviewsBlock = driver.find_elements_by_css_selector('.gws-localreviews__general-reviews-block')[1];
    reviews = driver.find_elements_by_css_selector('.gws-localreviews__google-review');
    
    count = 0
    for r in reviews:
        driver.implicitly_wait(5)
        count+=1
        if count < 4 :   #前三則評論重複 從第四則開始抓
            continue
        
        reviewBlock = r.find_element_by_css_selector('.Jtu6Td');
        if reviewBlock.find_element_by_css_selector('span').text.find(' ⋯⋯更多') == -1: # .find(' ⋯⋯更多')== -1 回傳-1就是找不到唷
            comment = reviewBlock.find_element_by_css_selector('span').text
            if comment != 0:
                comment_list.append(comment)
        else:
            comment = reviewBlock.find_element_by_css_selector('span').text.split(' ⋯⋯更多')[1]
            if comment != 0:
                comment_list.append(comment)
    userreview.append([name,h_score, comment_list,count])
    

    print("共" + str(count) + "筆")
    driver.quit()
    print('driver quit')


import pandas
df = pandas.DataFrame(userreview)
df.columns = ['hospital', 'score', 'comment',"筆數"]
df.to_csv('C:/Users/USER/Downloads/5.csv',encoding='utf8',index=False)

print('**ALL DONE');



