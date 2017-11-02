# Machine Learning
[機器學習詳細的分類](#Types of Machine Learning)
</br>
[評估機器學習演算法](#Hoeffdings inequality)


![](/assets/gm9wDgD.png)

## 什麼時候可以使用機器學習？
#### 1.要有規則 2.不容易寫出來的規則(辨識圖片)3.有足夠的資料
## 機器學習作法？
#### 從資料出發去學習
---
## Learning Model
#### D:跟f有關的資料 
#### A:機器學習的演算法 
#### H:A演算法裡面有很多假說 
#### g:接近真實f的演算法(函數) 
#### f:夢想得到的演算法(函數)




#### 目標：從A裡面很多個H中選一個來代表g,希望g越接近f
 

![](/assets/sswd.PNG)

---

# Types of Machine Learning
<a id="Types of Machine Learning"></a>

## 1.Learning with Different Output Space(要問什麼問題)
</br>

| Binary Classification | Multiclass classification |Regression|Structured Learning|
| :--- | :--- |:--- |:--- |
| ![](/assets/binary_perceptron.PNG) | ![](/assets/3擷取.PNG) |![](/assets/擷取選取區域_051.png)|![](/assets/擷取選取區域_052.png)|
## 2.Learning with Different Data Label(拿到不同標記的資料,要怎處理)
</br>

|Supervised|Semi-supervised|Unsupervised|Reinforcement Learning (增強式學習)|
| :--- || :--- || :--- || :---|
|Sample:Classification![](/assets/3擷取.PNG) |![](/assets/擷取選取區域_056.png)| Sample: Clustering![](/assets/擷取選取區域_055.png)</br>clustering(分群)</br>density estimation:哪些地方比較稠密應用ex.哪裡比較常發生事故</br>outlier detection:找出異常的資料,因為異常資料很少|跟訓練寵物一樣,對給獎勵,錯給懲罰
|
## 3 Learning with Different Protocol $$f \implies (x_{n},y_{n})$$輸入資料的方法
</br>

|batch| Online|active|
|:---|:---|:---|
|成批的資料來學習|一筆一筆資料來學習,遇到錯誤在改正</br>ex.PLA,Reinforcement Learning|機器自己問問題,當資料很少或很貴可以使用,也希望機器學習速度加快跟人一樣</br>ex.機器自己寫一個數字,反過來問人來學習|
## 4 Learning with Different Input Space $$\mathcal{X}$$ 資料種類
</br>

|Concrete| Raw|abstract|
|:---|:---|:---|
|資料裡面有人類的智慧,有預先處理的資料</br>範例:辨識1跟5 用人腦寫下規則到底這張圖有沒有對稱或是密度如何![](/assets/擷取選取區域_057.png)|原始的資料,音訊,bit,pixel</br> 範例:直接輸入pixel,但pixel沒有人類智慧只是單純的數據![](/assets/擷取選取區域_058.png)|抽象的資料ex.使用者id編號|

---
<a id="Hoeffdings inequality">
## Verification 評估演算法好不好
</a>



### Choose ONE hypothesis set using Hoeffding's inequality
![](/assets/hi.PNG)

###Choose many hypothesis set
![](/assets/HF2.JPG)

hypothesis set越大,所需要的資料(N)就越大,才能符合準確度


[Hoeffding's inequality(詳細評估機器學習演算法的方法)
](/mathematics/probability-theory/hoeffdings-inequality.md)

