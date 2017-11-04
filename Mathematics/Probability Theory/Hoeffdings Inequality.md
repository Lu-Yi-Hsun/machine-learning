 # Hoeffding's inequality 應用：演算法的評估 {#top}

## 目錄

* ### [Hoeffding's inequality基本概念](#hisample)

* ### [Hoeffding's inequality應用在機器學習](#himl)
    * #### [解釋符號](#sigdec)
    * #### [單一Hypothesis](#onehiml)
    * #### [多Hypothesis](#muhiml)
    * #### [遇到無限Hypothesis的問題](#nonlimhiml)

---

# Hoeffding's inequality基本概念 {#hisample}

[top](#top)

### 這裡以彈珠做舉例

![](/assets/hZ4lFY6.png)

### 抽一次誤差很大的機率很低,該不等式能說明該機率有多低

* 符號解釋
    * N=抽出多少個
    * $$\nu$$=橘色機率在N中
    * $$\mu$$=橘色的機率占全部\(通常未知\)
    * $$\epsilon$$=$$\nu$$跟$$\mu$$的誤差
* 固定$$\epsilon$$,一次抽越多樣本$$\epsilon$$\(誤差\)機率越小
* 固定N,$$\epsilon$$\(誤差\)越大的機率越小
* 證明!抽出的越多\(N越大\)$$\nu$$跟$$\mu$$越接近

![](/assets/擷取選取區域_063.png)
$$\nu$$和$$\mu$$大概差不多是對的,在$$\epsilon$$容忍誤差內
* probably:大概
* approximately:差不多
  ### 練習題

  ![](/assets/ff.PNG)

---

# Hoeffding's inequality應用在機器學習 {#himl}
[top](#top)

* ##符號解釋：{#sigdec}
    * ## $$\nu \implies E_{in}(h)$$:在已知的資料內,該演算法目前犯錯的機率(越小準確率越高)
    * ## $$\mu\implies E_{out}(h)$$:該演算法在"全部"資料(上帝視角)內犯錯的機率(同常未知)
    * ## $$N$$:資料數量
    * ##$$M$$:Hypothesis假說的數量
    * ##$$\color{red}{Bad}:E_{in}$$跟$$E_{out}$$誤差大於$$\epsilon$$的情況
---
## 單一Hypothesis {#onehiml}
用途:確認該Hypothesis好不好

[top](#top)
### 接下來會改寫剛剛的基本概念,改寫成這個公式
![](/assets/擷取選取區域_060.png)
### Hypothesis說明當我只有一個h（Hypothesis）,從這麼多個$$D$$抽到$$\color{red}{Bad}$$的機率小於等於$$2e^{-2\epsilon^{2}N}$$
### $$D_{n}$$:每次抽出的資料 
![](/assets/擷取選取區域_065.png)
  
![](/assets/擷取選取區域_061.png)

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig = plt.figure()
fig.suptitle(r'$\mathbb{P}[|E_{in}(h)-E_{out}(h)|>\epsilon]\leq2e^{-2\epsilon^{2}N}$',fontsize=20,color="gray")


#FIG1
plt.subplot(1, 2, 1)
N=1000
e=np.arange(0,1,0.00001)
y= 2*np.exp((-2*e**2)*N)
for i in y:
    if i<0.1:
        print(i)
        plt.plot(np.arange(0,1,0.00001),i*np.ones(len(np.arange(0,1,0.00001))),"r-",label=r"$\mathbb{P}$<=0.1")
        break
plt.xlabel("ε")
plt.ylabel("$\mathbb{P}$")
plt.plot(e,y,color='b',alpha=1,label="N="+str(N))
plt.legend()

#FIG2
plt.subplot(1, 2, 2)
e=0.1
N=np.arange(0,1000,1)
y= 2*np.exp((-2*e**2)*N)
for i in y:
    if i<0.1:
        print(i)
        plt.plot(np.arange(0,1000,1),i*np.ones(1000),"r-",label=r"$\mathbb{P}$<=0.1")
        break


plt.plot(N,y,"b-",label="e="+str(e))
plt.legend()
plt.xlabel("N")
plt.ylabel("$\mathbb{P}$")
plt.tight_layout()


plt.subplots_adjust(top=0.8)

plt.show()
```
### 練習題
![](/assets/擷取選取區域_064.png)
#### 題目：你的朋友發現一個股市的規則"當早上上漲 下午就下跌",為了確認這條規則你就從過去十年資料裡面抽出100筆資料,發現80筆是正確的,什麼結論你可以說?
#### 1.藉由利用該規則在未來的100天賺錢,你"肯定"將會變成有錢人(不能這麼肯定)
#### 2.當未來100天股市走勢與十年以來的歷史資料很接近,利用該規則在未來的100天賺錢,你"很可能"會變成有錢人(正確)
#### 3.藉由從20個朋友裡面選一個最好的規則,來當作投資未來100天股市的方法,你很有可能變成有錢人(錯！因為Hypothesis只有一個（"當早上上漲 下午就下跌"）不能選擇)
#### 4.你肯定會變有錢人,如果你以前就使用該規則(錯 因為你只是抽出100天來做分佈,搞不好十年來的資料分佈很不一樣)
---
## 多個hypothesis set {#muhiml}

[top](#top)

用途：當hypothesis有限,可以確認該機器學習演算法好不好
###推導多個hypothesis set公式
![](/assets/擷取選取區域_066.png)
![](/assets/擷取選取區域_067.png)
### 可以設定hypothesis set有多少 可以計算出當你的hypothesis set越大 N就要越大,資料才會準確
![](/assets/擷取選取區域_068.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
#equation title
plt.xlabel('$\epsilon$')
fig.suptitle(r'$\mathbb{P}[|E_{in}(h)-E_{out}(h)|>\epsilon]\leq$2$Me^{-2\epsilon^{2}N}$',fontsize=20,color="black",alpha=0.6)
plt.subplots_adjust(left=0.25, bottom=0.25)
hypothesis=1 #set how many hypothesis set
x = np.arange(0.0, 1.0, 0.001)

a0 = 5


s=2*hypothesis*np.exp((-2*x**2)*a0)
l, = plt.plot(x, s, lw=2, color='red')
#plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'

axamp = plt.axes([0.25, 0.09, 0.65, 0.03], facecolor=axcolor)


samp = Slider(axamp, 'N', 0.0, 1000.0, valinit=a0)



hy = plt.axes([0.25, 0.13, 0.65, 0.03], facecolor=axcolor)


hy_ok = Slider(hy, 'Hypothesis set(M)', 0.0, 1000.0, valinit=hypothesis)


def update(val):
    amp = samp.val
    hyy=hy_ok.val
    l.set_ydata(2*hyy*np.exp((-2*x**2)*amp))
    fig.canvas.draw_idle()

samp.on_changed(update)
hy_ok.on_changed(update)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    hy_ok.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)



def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)


plt.show()
```
### 練習題1
![](/assets/擷取選取區域_069.png)
###題目:請選出錯誤的
### 1.因為$$x_{1}$$跟$$x_{2}$$不同所以$$h_{1}$$跟$$h_{2}$$不同
### 2.雖然$$h_{1}$$跟$$h_{3}$$輸入不完全一樣但是因為只差正負號所以裡面資料的比例還是一樣
### 3.按照題目來說hypothesis有四個帶入公式就如題
### 4.但是由於資料正負的關西$$h_{1}=h_{3},h_{2}=h_{4}$$所以扣掉重複的部份,hypothesis剩下兩個所以該題也正確（之後會利用刪去重複的部份來求出當遇到無限個hypothesis時該怎麼解決）

###練習題2
![](/assets/HF3.JPG)  
### 題目:要符合E$$\tiny{in}$$和E$$\tiny{out}$$誤差超過0.1\($$\epsilon$$\)的機率小於等於0.05\($$\delta$$\)hypothesis set有100個\(M\)我的N最少要幾個


答案為2

---

# \*遇到無限Hypothesis的問題 {#nonlimhiml}

## PLA演算法的hypothesis set有無限多所以怎麼辦?

因為在平面上有無限多條線所以pla的hypothesis set有無限多個那該怎計算?  
因為有許多重疊的hypothesis set  
底下把hypothesis set用dichotomy來替換,因為hypothesis set無限多無法計算  
以PLA舉例:  
![](/assets/DI.JPG)

* hypothesis set 所有可能的線\(以上圖來說有無限多種來分開一個點\)
* dichotomy 資料分群的方法\(有兩種方法上圖的兩條線\)

  ## 所以要算出真正的成長函數\(需要用到機率的知識\)

  [影片](https://www.youtube.com/watch?v=dnVofdAomWY&list=PLXVfgk9fNX2I7tB6oIINGBmW50rrmFTqf&index=20)

* $$\tiny{H}(N)$$:dichotomy

* break point:第一次有發生"全部"無法解決的N\(只要找到一個排列都可以解決就不是breakpoint\)

  ## break point 計算方法

  #### 例如perceptrons

* 這個形狀下的排列每個都可以用一條線分開所以breakpoint不是3  
  ![](/assets/bb1.JPG)

* 這個形狀下發生無法用線分開,其他形狀也發生無法全部分開所以breakpoint為4  
  ![](/assets/bb2.JPG)

| m$$\tiny{H}(N)$$=O\($$N^{breakpoint-1}$$\) | positive rays | positive intervals | convex | 2D perceptrons |
| :--- | :--- | :--- | :--- | :--- |
| m$$\tiny{H}(N)$$ | N+1 =O\(N\) | $$\frac{1}{2}N^2+\frac{1}{2}N+1$$=O\($$N^2$$\) | $$2^N$$ | $$O(N^3$$\) |
| break point | 2 | 3 | None | 4 |

# 最後如果要用dichotomy取代hypothesis set

![](/assets/HF5.JPG)  
[證明上圖](https://www.csie.ntu.edu.tw/~htlin/course/ml08fall/doc/vc_proof.pdf)

---



