# -*- coding: utf-8 -*-
"""
https://contest.yandex.ru/contest/12341/problems/D/
"""
import random

def Foo(a): 
    result = 0  
    while len(a) > 2:           # пока длина массива больше двух элементов  
      a.sort()                # отсортировать массив по возрастанию элементов  
      n = len(a)  
      x = a[0] + a[n - 2]  
      result += x               # добавить x к накапливаемому результату  
      del a[n-2]                # удалить элемент по индексу (n-2)  
      del a[0]                  # удалить элемент по индексу 0  
      a.append(x)               # добавить элемент со значением x в конец массива  

    return sum(a) + result      # к накапливаемому результату добавить сумму элементов

def Foo_opt(a):
    a.sort()
    n=len(a)
    result=0
    sum_n1=a[n-1]
    sum_n2=a[n-2]
    b=0
    for i in range(n-2):
        if sum_n2<sum_n1:
            sum_n2+=a[i]
            result+=sum_n2
        else:
            sum_n1+=a[i]
            result+=sum_n1
       
    
    return sum(a)+result

#a="3 6 2018"
#b=[int(x) for x in a.split(" ")]
b=[random.randint(0,1000000) for i in range(300000)]
print(Foo_opt(b))
