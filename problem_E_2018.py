# -*- coding: utf-8 -*-
"""
https://contest.yandex.ru/contest/12341/problems/E/
"""
import numpy as np
    
class labyrinth:
       
    def __init__(self, string):
        self.string=string
        self.m = len(string.split('\n')[1:-1])
        self.n = len(string.split('\n')[1])
        self.chararray=self.from_string_to_chararray(string)

        
    def __str__(self): 
       return self.string
        
    def from_string_to_chararray(self, string):
        list_=string.split('\n')[1:-1]
        chararray=np.chararray((self.m, self.n),unicode=True)
        for x in range(self.m):
            for y in range(self.n):
                chararray[x][y]=list_[x][y]
        return chararray
    
    def from_chararray_to_string(self, chararray):
        string_=[]
        for x in range(self.m):
            string_.append('\n')
            for y in range(self.n):
                string_.append(chararray[x][y])
        string_.append('\n')
        
        return ''.join([str(x) for x in string_])
    
    
    
    def is_connected(self, point_a, point_b, chararray):
        connected_points=set()
        connected_points.add(point_a)
        def check_neighbors(point):
            if chararray[point[0]+1][point[1]]=='.' and (point[0]+1,point[1]) not in connected_points:
                connected_points.add((point[0]+1,point[1]))
                check_neighbors((point[0]+1,point[1]))
            if chararray[point[0]-1][point[1]]=='.' and (point[0]-1,point[1]) not in connected_points:
                connected_points.add((point[0]-1,point[1]))
                check_neighbors((point[0]-1,point[1]))            
            if chararray[point[0]][point[1]-1]=='.' and (point[0],point[1]-1) not in connected_points:
                connected_points.add((point[0],point[1]-1))
                check_neighbors((point[0],point[1]-1))            
            if chararray[point[0]][point[1]+1]=='.' and (point[0],point[1]+1) not in connected_points:
                connected_points.add((point[0],point[1]+1))
                check_neighbors((point[0],point[1]+1)) 

            
        check_neighbors(point_a)
            
        return point_b in connected_points
    
    def connect_points(self, point_a, point_b, chararray):
        chararray[int((point_a[0]+point_b[0])/2)][int((point_a[1]+point_b[1])/2)]='.'
        return chararray
    
    def connected_version(self):
        chararray=self.chararray
        for x in range(1, self.m-1, 2):
            for y in range(1, self.n-1,2):
                #print(x,y)
                #print(self.from_chararray_to_string(chararray))
                if y+2>=self.n:
                    pass
                elif self.is_connected((x,y),(x,y+2),chararray)==False:
                    chararray=self.connect_points((x,y),(x,y+2),chararray)
                    #print(self.from_chararray_to_string(chararray))
                    
                if x+2>=self.m:
                    pass
                elif self.is_connected((x,y),(x+2,y),chararray)==False:
                    chararray=self.connect_points((x,y),(x+2,y),chararray)
                    #print(self.from_chararray_to_string(chararray))
        return chararray
        
    def connect(self):
        self.chararray=self.connected_version()
        self.string=self.from_chararray_to_string(self.chararray)



string="""
+-+-+-+
|.|...|
+-+-+-+
|.|...|
+-+-+-+
"""

a=labyrinth(string)
print(a.string)
print(a.from_chararray_to_string(a.connected_version()))

"""
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.|...|
+-+-+-+-+-+-+
|.|...|.....|
+-+-+-+-+-+-+
"""