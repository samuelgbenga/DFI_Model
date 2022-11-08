#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:11:38 2022

@author: samuel
"""

import pandas as pd
import pprint
import os

#filename='logfile.pcap'
def GetInfo():
    os.system('tshark -r logfile.pcap > raw_data.txt')
    filepath = "./raw_data.txt"
    file = open(filepath, "r")
    raw_data = file.read()
    raw_data = raw_data.split("\n")
    raw_data.pop()
    # loop through
# =============================================================================
#     for elem in raw_data:
#          print(elem)
# =============================================================================
         
    return(raw_data)
    

# GetInfo()
#df = pd.read_csv(filepath, header=None)
# =============================================================================
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 150)
# =============================================================================
#df = pd.read_csv(filepath, header=None)

#print(df)

#print(df.shape)
#print(df.shape)