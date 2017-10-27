 # Binary Classification/二元分類 PLA 
###用一條線分開數據
---

### 核心演算法

| 找到一條線能分開兩種結果 | 如何修改線 |
| :---: | :---: |
| ![](/assets/figure_1.png) | ![](/assets/RUNXN76.png) |

可以容錯是pla變形演算法叫pocket
```python
import matplotlib.pyplot as plt
import numpy as np

#網路上找的dataset 可以線性分割

dataset = np.array([
((1, 1, 5), -1),
((1, 2, 4), -1),
((1, 3, 3), -1),
((1, 4, 2), -1),
((1, 1, 6), 1),
((1, 2, 5), 1),
((1, 3, 4), 1),
((1, 4, 3), 1)])
# 1 mean to display -c/b if c=0 i was error
# ax+by+c=0
#y=(-a/b)x+(-c/b)
#
#判斷有沒有分類錯誤，並列印錯誤率

def check_error(w, dataset):
    result = None
    error = 0
    for x, s in dataset:
        x = np.array(x)
        print(w.T.dot(x))
        if int(np.sign(w.T.dot(x))) != s:
            #帶入ax+by+c=0 如果符號不相等代表有錯誤

            # T transpose
            result =  x, s
            error += 1
    print  ("error=%s/%s" % (error, len(dataset)))
    return result

#PLA演算法實作
#Cyclic PLA
def pla(dataset):

    #ax+by+c=0 線性方程式的法向量
    w = np.zeros(3)#法向量
    index=0
    while check_error(w, dataset) is not None:
        

        x, s = check_error(w, dataset)
        w += (s) * x
        #fig by algorithm(1).md
        index=index+1
        
    return w


def print_image(w):
 
    #畫圖
    ps = [v[0] for v in dataset]
    value = [v[1] for v in dataset]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #111 is control code 1
    #These are subplot grid parameters encoded as a single integer. For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
    #dataset前半後半已經分割好 直接畫就是
    index=0
    
    max_x=ps[0][1]
    min_x=ps[0][1]
    for v in value:
        #print(index)
        if v>0:
            ax1.scatter(ps[index][1],ps[index][2], c='b', marker="o")
        elif v<0:
            ax1.scatter(ps[index][1],ps[index][2] , c='r', marker="x")
        else:
            pass
        if max_x<ps[index][1]:
            max_x=ps[index][1]
        if min_x>ps[index][1]:
            min_x=ps[index][1]
        index=index+1
    
    l = np.linspace(min_x-1,max_x+1)
    #define the line x-axis size
    a,b = -w[1]/w[2], -w[0]/w[2]
    #a=斜率 b常數
    ax1.plot(l, a*l + b, 'b-')
     
    plt.show()


w = pla(dataset)
print_image(w)
```
#優化版本(2段程式碼)
###耗時1/3

```python
import matplotlib.pyplot as plt
import numpy as np
import random
#網路上找的dataset 可以線性分割

dataset = np.array([
((1, 1.6, 5), -1),
((1, 2, 4), -1),
((1, 3, 3), -1),
((1, 4, 2), -1),
((1, 1, 6), 1),
((1, 2, 5), 1),
((1, 3, 4), 1),
((1, 4, 3), 1)])
# 1 mean to display -c/b if c=0 i was error
# ax+by+c=0
#y=(-a/b)x+(-c/b)
#
#判斷有沒有分類錯誤，並列印錯誤率
bad=0
def check_error(w, dataset):
    result = None
    result=[]
    error = 0
    for x, s in dataset:
        x = np.array(x)
        print(w.T.dot(x))
        if int(np.sign(w.T.dot(x))) != s:
            #帶入ax+by+c=0 如果符號不相等代表有錯誤

            # T transpose
            tem=[]
            tem.append(x)

            tem.append(s)

            result.append(tem)
            
            error += 1
    print  ("error=%s/%s" % (error, len(dataset)))
    bad=error/len(dataset)
    
    if error==0:
        result=None
        return result
      
    #優化區塊1 每次選擇的錯誤用隨機所以不會一樣
##############################################
    return result[random.randrange(0,error, 1)]

#PLA演算法實作
#Cyclic PLA
def pla(dataset):

    #ax+by+c=0 線性方程式
    w = np.zeros(3)
    ax,plt=print_image(w)
    #print (w)
    
    index=0
    while check_error(w, dataset) is not None:


        x, s = check_error(w, dataset)
        ##優化區塊2 把baise用隨機 讓它變動快點
        x[0]=(1-bad)*x[0]*random.uniform(1,4)
        #############################################
        w += (s) * x
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        l = np.linspace(0,4)
        #define the line x-axis size
        a,b = -w[1]/w[2], -w[0]/w[2]
        #a=斜率 b常數
        lines=ax.plot(l, a*l + b, 'b-')
        #plt.pause(0.1)
         
        print (w)
        index=index+1
    print ("all run circel")
    print (index)
    plt.pause(111)
    return w


def print_image(w):

    #畫圖
    ps = [v[0] for v in dataset]
    value = [v[1] for v in dataset]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #111 is control code 1
    #These are subplot grid parameters encoded as a single integer. For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
    #dataset前半後半已經分割好 直接畫就是
    index=0

    max_x=ps[0][1]
    min_x=ps[0][1]
    for v in value:
        #print(index)
        if v>0:
            ax1.scatter(ps[index][1],ps[index][2], c='b', marker="o")
        elif v<0:
            ax1.scatter(ps[index][1],ps[index][2] , c='r', marker="x")
        else:
            pass
        if max_x<ps[index][1]:
            max_x=ps[index][1]
        if min_x>ps[index][1]:
            min_x=ps[index][1]
        index=index+1

    l = np.linspace(min_x-1,max_x+1)
    #define the line x-axis size
    a,b = -w[1]/w[2], -w[0]/w[2]
    #a=斜率 b常數
    ax1.plot(l, a*l + b, 'b-')
    plt.ion()
    plt.show()
    return ax1,plt

w = pla(dataset)
print_image(w)

```


#當線性可分的時候:證明PLA演算法在有限時間內一定會找到一條最好的直線









 












