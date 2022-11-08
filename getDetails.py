#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 03:59:42 2022

@author: samuel
"""
import pandas as pd
import pprint
import os

#filename='logfile.pcap'

os.system('tshark -r logfile.pcap > raw_data.csv')


filepath = "./raw_data.csv"

#df = pd.read_csv(filepath, header=None)
df = pd.read_csv(filepath)
#print(df)

#print(df.shape)
print(df.shape)
detail_list = []

for row in df.iterrows():
    detail_list.append(row)



# convet tuples to string function
def ConvertToString(tuples):
    st = str(tuples)
    return st

#result = str(detail_list[1])
#result = ConvertToString(detail_list[1])
#print(result)

#print(type(result))

# convert sting to list
def Convert(string):
    li = list(string.split(" "))
    return li

#new_result = Convert(result)

# function to clearn the list or redundant info
def CleanList(l):
    result = []
    
    for idx, elem in enumerate(l):
        if idx >= 1 and idx < len(l) - 6:
            if len(elem) > 1:
                result.append(elem.replace("\n", ""))
                #print(elem)
    return result

#n_result = CleanList(new_result)
    

# loop through every clean data
# =============================================================================
# def PrintResult(result):
#         #for elem in result:
#             #print(elem)
#         # just print element array
#         print(result)
#         #print length of array
#        # print("\nthe length is", len(result))
#         
# =============================================================================
        
        




#print(new_result1)   

def RunCode(number):
    # call convert to string result code
    result = ConvertToString(detail_list[number])
    
    #call convert result code
    new_result = Convert(result)
    
    #call clearnList function
    #n_result = CleanList(new_result)
    n_result = CleanList(new_result)
    
    # PrintResult(n_result)
    # print(number)
    #print(n_result)
    return n_result
    














































