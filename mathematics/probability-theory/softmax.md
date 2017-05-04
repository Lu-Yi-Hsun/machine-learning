# Softmax
#####把數值依據比例壓縮至1
#####例:scores = [2.0, 1.0, 0.2]=>[ 0.65223985  0.23994563  0.10781452]
$$\sigma$$\(z\)$$\tiny{j}$$=$$\tfrac{e^{\Large{z}\tiny{j}}}{\sum_{k=1}^Ne^{\Large{z}\tiny{k}}}$$

```python
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x)
    return e_x / e_x.sum()

scores = [2.0, 1.0, 0.2]
print(softmax(scores))
```



