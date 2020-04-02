
"""
https://contest.yandex.ru/contest/12341/problems/B/
"""
import numpy as np

def pokrytie(n,list_):
    
    def spec(di, white):
        if di==0:
            return 1
        elif white==1:
            return 1
        else:
            return 2**di    

    if n>1:
        return spec(list_[0],0)*pokrytie(n-1,list_[1:])+spec(list_[0],1)*spec(list_[1],0)*pokrytie(n-2,list_[2:])
    elif n==1:
        return 2
    else:
        return 1
   


a="0 3 0 1 2 1 3 1 0"
b=[int(x) for x in a.split(" ")]
print(pokrytie(len(b), b)%1000000007)
