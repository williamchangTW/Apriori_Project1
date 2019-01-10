# Association_Analysis
利用IBM Quest Synthetic Data Generator 來產生隨機的資料集，並用於關聯性分析  
在main.py中實作以下幾點  
1. 資料的前處理  
2. 轉換資料為離散型態，以供WEKA使用  
3. 利用兩個Apriori Algorithm進行關聯性分析  
4. 利用FP-Growth進行關聯性分析  

最後利用WEKA內建的Apriori分析進行分析  
![image](https://github.com/twngbm/Association_Analysis/blob/master/WEKA.jpg)

# 分析:  
1. 不同實作方法的Apriori Algorithm，由於演算法相同的緣故，因此得出的結果相同，惟實作方法不同，在效能上略有差異  
2. 利用WEKA可以得出類似的關聯性法則
