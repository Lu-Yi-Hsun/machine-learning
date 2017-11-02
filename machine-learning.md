# Machine Learning{#top}
##目錄
###[概論](#概論)

###[Learning Model](#LearningModel)

###[機器學習詳細的分類](#TofML)

###[評估機器學習演算法](#HI)

---
#概論{#概論}

[top](#top)


![](/assets/gm9wDgD.png)

## 什麼時候可以使用機器學習？
### 1.要有規則 2.不容易寫出來的規則(辨識圖片)3.有足夠的資料
## 機器學習作法？
### 從資料出發去學習
---
# Learning Model{#LearningModel}
[top](#top)

### 目標：從A裡面很多個H中選一個來代表g,希望g越接近f
## D:跟f有關的資料 
## A:機器學習的演算法 
## H:A演算法裡面有很多假說 
## g:接近真實f的演算法(函數) 
## f:夢想得到的演算法(函數)

 

![](/assets/sswd.PNG)

---

# Types of Machine Learning{#TofML}
[top](#top)


 

## 1.Learning with Different Output Space(要問什麼問題)


| Binary Classification | Multiclass classification |Regression|Structured Learning|
| :--- | :--- |:--- |:--- |
| ![](/assets/binary_perceptron.PNG) | ![](/assets/3擷取.PNG) |![](/assets/擷取選取區域_051.png)|![](/assets/擷取選取區域_052.png)|
## 2.Learning with Different Data Label(拿到不同標記的資料,要怎處理)



|Supervised$$~~~~~~~~~~~~~~~~~~~~~~~~~~$$|Semi-supervised$$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$$|Unsupervised|Reinforcement Learning (增強式學習)|
| :--- || :--- || :--- || :--|
|Sample:Classification ![](/assets/3擷取.PNG) |![](/assets/擷取選取區域_056.png)| Sample: Clustering <br />![](/assets/擷取選取區域_055.png)<br />clustering(分群)density estimation:哪些地方比較稠密應用ex.哪裡比較常發生事故outlier detection:找出異常的資料,因為異常資料很少|跟訓練寵物一樣,對給獎勵,錯給懲罰
|
## 3 Learning with Different Protocol $$f \implies (x_{n},y_{n})$$輸入資料的方法


|batch| Online|active|
|:---|:---|:---|
|成批的資料來學習|一筆一筆資料來學習,遇到錯誤在改正ex.PLA,Reinforcement Learning|機器自己問問題,當資料很少或很貴可以使用,也希望機器學習速度加快跟人一樣ex.機器自己寫一個數字,反過來問人來學習|
## 4 Learning with Different Input Space $$\mathcal{X}$$ 資料種類


|Concrete| Raw|abstract|
|:---|:---|:---|
|資料裡面有人類的智慧,有預先處理的資料,範例:辨識1跟5 用人腦寫下規則到底這張圖有沒有對稱或是密度如何![](/assets/擷取選取區域_057.png)|原始的資料,音訊,bit,pixel,範例:直接輸入pixel,但pixel沒有人類智慧只是單純的數據![](/assets/擷取選取區域_058.png)|抽象的資料ex.使用者id編號|

---
# 評估機器學習演算法{#HI}
[top](#top)
##問題：到底機器學習從資料裡面能不能學到東西並且預測？
## 1."目前"看起來機器學習無法從資料來預測未知

![](/assets/擷取選取區域_059.png)
###雖然在已看過得資料內g=f,但是未看過的資料內無法保證g=f,所以"目前"只能說機器學習可能學不到東西
####g:機器學習學到的方程式 f:夢想求出的方程式
##2.使用Hoeffding's inequality就能證明機器學習能學到東西並且預測未知
##Verification 評估演算法好不好






### Choose ONE hypothesis set using Hoeffding's inequality
![](/assets/hi.PNG)

###Choose many hypothesis set
![](/assets/HF2.JPG)

hypothesis set越大,所需要的資料(N)就越大,才能符合準確度


[Hoeffding's inequality(詳細評估機器學習演算法的方法)
](/mathematics/probability-theory/hoeffdings-inequality.md)

