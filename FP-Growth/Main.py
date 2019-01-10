from itertools import permutations
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori
import pyfpgrowth

#Data_Preprocessing
f=open("data.ntrans_1.nitems_0.01.txt")
data_set=[]
Association=[]
now="1"
for line in f:
    if now==line[9]:
        Association.append(int(line[31]))
    else:
        data_set.append(Association)
        Association=[]
        now=line[9]
        Association.append(int(line[31]))
f.close()

#transform data to feet Weka
d={'0':[0 for i in range(len(data_set))],'1':[0 for i in range(len(data_set))],'2':[0 for i in range(len(data_set))],'3':[0 for i in range(len(data_set))],'4':[0 for i in range(len(data_set))],'5':[0 for i in range(len(data_set))],'6':[0 for i in range(len(data_set))],'7':[0 for i in range(len(data_set))],'8':[0 for i in range(len(data_set))],'9':[0 for i in range(len(data_set))]}
df=pd.DataFrame(data=d)
index=0
for i in data_set:
    for j in i:
        df.iat[index,j]=1
    index+=1
df.to_csv("data_t.csv",index=False)

#Normal Apriori Algorithm
#Using  Libary Apyori
print("This part is Apriori that made by Apyori")
print("With Min support = 0.75 and confidence=0.5")
input("Press Any Key to continue")
association_rules = apriori(data_set,min_support=0.75,min_confidence=0.5)  
association_results = list(association_rules)  
for item in association_results:
    support=item[1]
    Association=list(item[0])
    print("Association Rule=",Association)
    print("Support=",support)
    for order in item[2]:
        print("For Subset",list(order[0]),",item added=",list(order[1]),",which confidence=",order[2])

#Normal Apriori Algorithm(Hand Made)
print("This part is also Apriori Algorithm that writen by myself.")
print("With Min support = 0.75 and confidence=0.5")
input("Press Any Key to Continue.")
support=0.75
confidence=0.5
lenth=len(data_set)
scaned=[]
dismess=[]
def support_count(target):
    k=0
    for item in data_set:
        if target in item:
            k+=1
    return k
def support_count_p(target):
    k=0
    for item in data_set:
        if not False in [x in item for x in target]:
            k+=1
    return k
def conf_count(target):
    s=0
    k=0
    if len(target)==1:
        return support_count(target[0])/lenth
    for item in data_set:
        if target[-1] in item:
            s+=1
        if  not False in [x in item for x in target]:
            k+=1
    
    return k/s
for item in data_set:
    for i in item:
        if i in scaned or i in dismess:
            continue
        if support_count(i)/lenth>support:
            scaned.append(i)
assoc_rule=[]
dismess=[]
for i in range(len(scaned)):
    n=i+1
    Permutations=list(permutations(scaned,n))
    for p in Permutations:
        if support_count_p(p)/lenth>support:
            if conf_count(p)>confidence:
                print("Support=",round(support_count_p(p)/lenth,4),"Confidence=",round(conf_count(p),4),"Association set=",p)
        
print("This part is Apriori Algorithm using FP-Grow.")
print("With Min support = 0.75")
input("Press Any Key to Continue.")
patterns = pyfpgrowth.find_frequent_patterns(data_set, 0.75)
rules = pyfpgrowth.generate_association_rules(patterns, 0.5)
for r in rules:
    print(r,"->",rules[r][0],rules[r][1])
