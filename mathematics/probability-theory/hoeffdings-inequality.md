# Hoeffding's inequality

![](/assets/hZ4lFY6.png)

### 抽一次誤差很大的機率很低
* N=抽出多少個,$$\nu$$=橘色機率在N中,$$\mu$$=橘色的機率占全部,$$\epsilon$$=誤差
* 固定$$\epsilon$$,一次抽越多樣本$$\epsilon$$(誤差)機率越小
* 固定N,$$\epsilon$$(誤差)越大的機率越小
* 證明!抽出的越多(N越大)$$\nu$$跟$$\mu$$越接近


##由於不知道$$\nu$$真實的值所以只能算大概的機率就使用此方法
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

