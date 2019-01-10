# FP-growth association analysis
- `1.txt`: 經由轉換所使用的資料集
- `setup.py`: 用來一開始設定環境用
- `fp_growth.py`: fp-growth 的實作程式

## 如何使用
### 安裝
- 下指令建立環境
`python setup.py install`
>若有發生問題加上 `sudo`
- 下指令設定 min_support 及資料集
`python -m fp_growth -s {minimum support} {path to CSV file}`
### 重要函事說明
- 為最主要去找出 frequent itemsets, 可以再命令列設定 min_support 值進行運算找出, 找車皆會大於該輸入值, 運算速度相較於 Apriori 快
`from fp_growth import find_frequent_itemsets
for itemset in find_frequent_itemsets(transactions, minsup):
    print itemset`

- 利用WEKA內建的Apriori分析進行分析  
![https://github.com/williamchangTW/Apriori_Project1/blob/master/FP-Growth/WEKA_tool.jpg]

# 分析:  
- WEKA 工具的輔助使用下, 可以得到與運算過後的關聯分析是否正確
- 基於 FP-Growth 的方法下大幅的降低運算時間, 但也發現一件事, 若 min_support 的下降會造成運算時間大幅的拉長, 在 brute force 得方法下尤為明顯, Apriori algo 與 FP-growth 之間的差別顯而易見(FP-groth 只掃兩次)

#### 參考資料
- [Enaeseth Github](http://github.com/enaeseth/)
