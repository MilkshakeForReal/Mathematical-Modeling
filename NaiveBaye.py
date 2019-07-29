# -*- coding: utf-8 -*-
"""

@author: Mloong
"""
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.N = None
        self.K = None
        self.S = None 
        self.y_ck = {}
        self.p_Y = {}
        self.p_XY = {}
        
    def fit(self, X, y):
        self.N = X.shape[0]
        self.S = X.shape[1]
        self.K = len(set(y))
        self.y_ck = sorted(set(y))
        self.p_XY = dict.fromkeys(range(self.S), {})
        
        for ck in self.y_ck:
            self.p_Y[ck] = np.count_nonzero(y == ck) / self.N
            for j in range(self.S):
                X_j = sorted(set(X[:, j]))
                if self.p_XY[j] == {}:
                    self.p_XY[j] = dict(zip(X_j, [{} for k in X_j]))
                for l in X_j:
                    self.p_XY[j][l][ck] = np.count_nonzero(X[y==ck,j]==l)\
                                            / self.p_Y[ck] /self.N
                            
    def predict(self, X_test, i = 0):
        #单条测试
        y_prob = {}
        for ck in self.y_ck:
            y_prob[ck] = self.p_Y[ck]
            for j in range(self.S):
                y_prob[ck] *= self.p_XY[j][X_test[i, j]][ck]
                
        return y_prob
    
X = np.array([[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
              ['S','M','M','S','S','S','M','M','L','L','L','M','M',
               'L','L']]).T
y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])

cla = NaiveBayes()
cla.fit(X, y)
cla.predict(np.array([['2','S']]))
