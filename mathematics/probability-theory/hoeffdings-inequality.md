# Hoeffding's inequality

![](/assets/hZ4lFY6.png)

### 抽一次誤差很大的機率很低

* EX.圖抽一次全綠色所以橘色機率$$\nu$$=0%,$$\epsilon$$=\|$$\nu$$-$$\mu$$\|,$$\epsilon$$會很大所以$$\mathbb{P}$$會很小




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

