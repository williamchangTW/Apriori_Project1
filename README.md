Implementation of Apriori Algorithm 
==========================================

contributed by <'williamchangTW'>

List of files
-------------
1. Apriori_algorithm.ipynb
2. FP-growth.ipynb
3. README(this file)
4. data.ntrans_0.1.nitems_0.01
5. test_data.csv
6. zoo.csv
7. data.csv

## Apriori_algorithim
-----
- Enviroment
	- IDE : *jupyter notebook*
	- OS : *MacOS*
	- Language : Python
		- Python version : *3.7*
		- Python package : *pandas*
		
- Parameters
	- *minSupport* = 0.5
	- *minConfidence* = 0.6
	
- Preprocessing
	- IBM Quest Synthetic Data Generator
		- options
			- -ntrans 0.1
			- -nitems 0.01
	- test data : 
		- zoo.csv
		- data.csv
		- test_data.csv		
### Installation
-----
- Install by command as below:
`python3 pip install jupyter notebook`
`python3 pip install pandas`
- When you finished, key a command to start coding:
`jupyter notebook`

#### Notes 
- 關聯的規則其實可以簡單分成兩項
	- 支持度 (Support): 同時購買尿布跟啤酒的機率/總資料數，通常會設定最小支持度 (minSupport) 去減少干擾數據
	- 信心度 (Confiddence): 同時購買尿布跟啤酒的機率/單獨購買尿布的資料數，想知道購買尿布時會連同啤酒一起買的可能性，判斷關聯度
- Apriori algorithm : 簡單的說，依據先前的知識推導，作為下一次判斷的基礎，最後得到最終的關聯性
	- 演進過程：
		- 暴力窮舉法 (Brute force)
		- Apriori algorithm
		- FP-growth
- 暴力窮舉法中找到擁有 minSupport 及 minConfidence 所設定的門檻值以上的配對，稱為頻繁項目集合 (frequent items)
- Apriori algorithm 優點在於可以根據以下兩點特性來增加速度
	- frequent itemset 的子集合必須是 frequent itemset 的集合
	- 根據第一點反之亦然
- 舉例
	- 假設有 A, B, C, D, E 五種商品：
		-1. 將所有資料依據出現的頻率排序，假設是 B>C>A>D>E
		-2. 篩選（看有無符合最小信心度和最小支持度）出符合條件的資料，也就是稱為第一層的頻繁項目集合，假設是 B, C, A, D
		-3. 在 2. 的基礎下列出兩樣商品所有可能的組合，BC, BA, BD, CA, CD, AD
		-4.（利用了 Apriori 性質，在找下一層，也就是更大的頻繁項目集合時只會考慮頻繁項目子集合，所以 E 已經出局了）
		-5. 篩選出第二層的頻繁項目集合，假設是 BC, BA, BD, CA
		-6. 在 4. 的基礎下列出三樣商品所有可能的組合，只有 BCA！
		-7.（因為 CD, AD 已經出局了，所以包含它們的 BCD, BAD, CAD 不合格）
		-8. 篩選出第三層的頻繁項目集合，假設 BCA 通過

## FP-growth
-----
- 跟 `Apriori algorithm` 相差在於不需要每一層在篩選前列出所有可能的集合，只需要掃過資料兩次即可，第一次畫出 FpTree (frequent pattern Tree)，第二次找出頻繁項目集合 FpGrowth (frequent pattern Growth)
- 流程
	1. 第一次掃資料、畫出樹來 FpTree（Frequent Pattern Tree）
	2. 和 Apriori 一樣將所有資料依據出現的頻率排序，篩選出頻繁項目集合
	3. 把第一項資料的內容物依照 1. 篩選好的排序後用指標串起來，就會形成彼此的父結點和孩子結點，最上端的父結點接在 null node 之下
	4. 第二項資料照做，但如果串的順序（特別指父結點）和前面的有重複就不會再加，只會把原本 node 中的 count+1，不一樣的（子結點）才會另外伸出來。如果一開始父結點就不同那就從 null 結點另外開一個
	5. 第二次掃資料、找出頻繁項目集合 FpGrowth（Frequent Pattern Growth）
	6. 從樹的底層（第一階段 1. 的頻率排序的最後一個，上圖的啤酒）往上找
	7. 上圖單元結構的 FpNode next 的作用就是把一樣的項目用指標（上圖的虛線）連在一起，方便一次找到全部的啤酒來分析
	8. 把最底層（啤酒）開始，從它開始往上接著的結點鏈們一條一條列出，當作分開的集合再畫顆條件樹去分析，從中找出頻繁項目集合。詳細原理太繁瑣就省去 QQ 有興趣可以看我上面貼的網址
	9. 完成之後就輪到次底層（尿布），用一樣的方法找到頻繁項目集合
	10. 一路搜索到最上頭

