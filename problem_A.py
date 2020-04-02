
"""
https://contest.yandex.ru/contest/12341/problems/A/
"""

import numpy as np

def max_count(int_list):
    max_count=0
    max_int=np.nan
    dict_={}
    for i in int_list:
        if i not in dict_.keys():
            dict_[i]=1
        else:
            dict_[i]=dict_[i]+1
            
        if dict_[i]>max_count:
            max_count=dict_[i]
            max_int=i
        
    return max_int


a=[1,1,2,2,2,3,666,12]
print(max_count(a))
        