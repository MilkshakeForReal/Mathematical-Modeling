import numpy as np
import time
import datetime

X = np.array([[3,3],
              [4,3],
              [1,1]], dtype = np.float32)

y = np.array([1,1,-1])

#感知机算法
def perceptron(X, y, learning_rate = 1):
    N, d = X.shape
    w = np.zeros((d,1))
    b = 0
    pre = X.dot(w) + b
    margin = pre.flatten() * y
    i = np.where(margin <= 0)[0]
    while len(i) != 0:
        i = i[0]
        w += learning_rate * y[i] * X[i].reshape(-1,1)
        b += learning_rate * y[i]
        pre = X.dot(w)+b
        margin = pre.flatten() * y
        i = np.where(margin <= 0)[0]
    return w, b
        
t1 = time.time()
w, b = perceptron(X, y, learning_rate = 1)
t2 = time.time()
print('It took {} to train.'.format(datetime.timedelta(seconds=t2-t1)))
#>>> It took 0:00:00.000994 to train.
