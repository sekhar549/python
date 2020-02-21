# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:37:49 2019

@author: Raj Kunnuru
"""



def rotate_right(arr,k):
    
    if k==0:
        return arr
    
    l =len(arr)
    
    return(arr[-k:]+arr[:l-k])

arr = [1,2,3,4,5,6,7]

k = 2

print(rotate_right(arr,3))
    
    
    
