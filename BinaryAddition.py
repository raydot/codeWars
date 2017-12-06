#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:54:19 2017

@author: dkanter
"""

def add_binary(a,b):
    #conversion from https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
    myVar = a + b
    myVar = bin(myVar)[2:].zfill(8)
    return myVar 


print(add_binary(2, 5))