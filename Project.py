# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 21:01:25 2022

@author: Sandeep
"""

pun=["'", '"', ",", ".", "!", ":", ";", '#', '@']
pos=[]
neg=[]
s=[]
tw_c=[]
re_c=[]
po=[]
ne=[]
def str_pun(s):
    s1=''
    for i in s:
        if i in pun:
            continue
        s1+=i
    return s1
def get_pos():
    for i in s:
        l=i.split()
        c=0
        for j in l:
            if j.lower() in pos or j in pos:
                c+=1
        po.append(c)
def get_neg():
    for i in s:
        l=i.split()
        c=0
        for j in l:
            if j.lower() in neg:
                c+=1
        ne.append(c)
#Reading data

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            pos.append(lin.strip())


with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            neg.append(lin.strip())

with open("project_twitter_data.csv") as pos_f:
    i=1
    for lin in pos_f:
        if i==1:
            i=2
            continue
        li=lin.split(",")
        s.append(str_pun(li[0]))
        tw_c.append(int(li[1]))
        re_c.append(int(li[2]))
get_pos()
get_neg()
#Writing data into csv file
import csv
with open("resulting_data.csv", "w", newline='') as fp:
    fn=['Number of retweets',  'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score']
    wr=csv.DictWriter(fp, fieldnames=fn)
    wr.writeheader()
    for i in range(19):
        wr.writerow({'Number of retweets':tw_c[i],  'Number of Replies':re_c[i], 'Positive Score':po[i], 'Negative Score':ne[i], 'Net Score':po[i]-ne[i]})
del pos_f,i,lin,li,fp


#Plotting
import pandas as pd
df=pd.read_csv("resulting_data.csv")
import matplotlib.pyplot as plt
x=df['Net Score']
y=df['Number of retweets']
plt.scatter(x,y)
plt.title("Twitter Data")
plt.xlabel("Net Score")
plt.ylabel("Number of retweets")
