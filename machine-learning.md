# Machine Learning
![](/assets/gm9wDgD.png)

## 什麼時候可以使用機器學習？
#### 1.要有規則 2.不容易寫出來的規則(辨識圖片)3.有足夠的資料
## 機器學習作法？
#### 從資料出發去學習

## Learning Model
#### D:跟f有關的資料 
#### A:機器學習的演算法 
#### H:A演算法裡面有很多假說 
#### g:接近真實f的演算法(函數) 
#### f:夢想得到的演算法(函數)




#### 目標：從A裡面很多個H中選一個來代表g,希望g越接近f
 

![](/assets/sswd.PNG)
## Types of Learning
#1.
| Binary Classification | Multiclass classification |Regression|Structured Learning|
| :--- | :--- |:--- |:--- |
| ![](/assets/binary_perceptron.PNG) | ![](/assets/3擷取.PNG) |![](/assets/擷取選取區域_051.png)|![](/assets/擷取選取區域_052.png)|
#2.
|Supervised|Unsupervised|
| :--- || :--- |
|Sample:Classification![](/assets/3擷取.PNG) | Sample: Clustering![](/assets/擷取選取區域_055.png)</br>clustering(分群)</br>density estimation:哪些地方比較稠密應用ex.哪裡比較常發生事故</br>outlier detection:找出異常的資料,因為異常資料很少|
## Verification
### Choose ONE hypothesis set using Hoeffding's inequality
![](/assets/hi.PNG)

###Choose many hypothesis set
![](/assets/HF2.JPG)

hypothesis set越大,所需要的資料(N)就越大,才能符合準確度


[Hoeffding's inequality(評估機器學習演算法的方法)
](/mathematics/probability-theory/hoeffdings-inequality.md)

