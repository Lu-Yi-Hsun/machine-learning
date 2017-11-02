# Hoeffding's inequality 應用：演算法的評估

## 單一hypothesis  set

![](/assets/hZ4lFY6.png)

### 抽一次誤差很大的機率很低

* N=抽出多少個,$$\nu$$=橘色機率在N中,$$\mu$$=橘色的機率占全部\(通常未知\),$$\epsilon$$=誤差
* 固定$$\epsilon$$,一次抽越多樣本$$\epsilon$$\(誤差\)機率越小
* 固定N,$$\epsilon$$\(誤差\)越大的機率越小
* 證明!抽出的越多\(N越大\)$$\nu$$跟$$\mu$$越接近

## 由於不知道$$\mu$$真實的值所以只能算大概的機率就使用此方法

![](/assets/ff.PNG)

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig = plt.figure()
fig.suptitle(r'$\mathbb{P}[|v-\mu|>\epsilon]\leq2e^{-2\epsilon^{2}N}$',fontsize=20,color="gray")


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

![](/assets/GnTGZPR.png)

---

## 多個hypothesis set

## 可以設定hypothesis set有多少 可以計算出當你的hypothesis set越大 N就要越大,資料才會準確

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
#equation title
plt.xlabel('$\epsilon$')
fig.suptitle(r'$\mathbb{P}[|v-\mu|>\epsilon]\leq$2H$e^{-2\epsilon^{2}N}$',fontsize=20,color="black",alpha=0.6)
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


hy_ok = Slider(hy, 'hypothesis set(H)', 0.0, 1000.0, valinit=hypothesis)


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

![](/assets/HY3.JPG)

### 題目:當E$$\tiny{in}$$和E$$\tiny{out}$$誤差超過0.1\($$\epsilon$$\)的機率為0.05\($$\delta$$\)hypothesis set有100個\(M\)

![](/assets/HF3.JPG)  
答案為2

---

# PLA演算法的hypothesis set有無限多所以怎麼辦?

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



