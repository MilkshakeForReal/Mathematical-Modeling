# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:20:05 2018

@author: lenovo
"""

def me_cut_rod(p,n):
    r = [float('-inf') for i in range(n+1)]
    return me_cut_aux(p, n, r)
    
def me_cut_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + me_cut_aux(p,n-i,r))
    r[n] = q
    return q

import numpy as np
def b_u_cut(p,n):
    r = np.zeros(n+1)
    s = np.zeros(n+1)
    r[0] = 0
    for j in range(1,n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q<p[i]+r[j-i]:
                q = p[i]+r[j-i]
                s[j]=i
        r[j] = q
    return r,s     
    
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
r,s = b_u_cut(p, 5)
s = s.astype(int)
n = 5
while(n>0):
    print(s[n])
    n = n-s[n]

print(me_cut_rod(p, 5))
print(b_u_cut(p, 5))