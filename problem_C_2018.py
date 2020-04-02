"""
https://contest.yandex.ru/contest/12341/problems/C/
``"""

import numpy as np
import math
from collections import Counter


def rozklad(n):
           
    if n==1:
        return {}
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += i%2+1
        else:
            n //= i
            factors.append(i) 
    if n > 1:
        factors.append(n)
    
    return Counter(factors)

def sklad(dict_):
    a=1
    for x in [i**dict_[i] for i in dict_.keys()]:
        a*=x
    return a

def sucet(dict_1,dict_2):
    for key in dict_2.keys():
        dict_1[key]=dict_1.get(key, 0)+dict_2[key]
    return dict_1
        
def rozdiel(dict_1,dict_2):
    dict_={}
    for key in set(list(dict_1.keys())+list(dict_2.keys())):
        a=dict_1.get(key, 0)-dict_2.get(key, 0)
        if a>0:
            dict_[key]=dict_1.get(key, 0)-dict_2.get(key, 0)
    return dict_

        
def comb(a,b):
    if b<=(a-b):
        hore={}
        dole={}
        for i in range(b):
            hore=sucet(hore,rozklad(a-i))
            dole=sucet(dole, rozklad(b-i))
            

        return rozdiel(hore,dole)
    else:
        return comb(a,a-b)

        

def euler_function(a,b):
    rozklad_n=comb(a,b)
    hore={}
    dole={}
    for i in rozklad_n.keys():
        hore=sucet(hore,rozklad(i-1))
        dole=sucet(dole, {i:1})
    return sklad(rozdiel(sucet(rozklad_n,hore), dole))

#for i in range(200000):
   #rozklad(500000-i)
  
#print(sklad(rozklad(50000)))
#omb(500000,200000)
#
print(math.log10(sklad(comb(500000,250000))))

    
