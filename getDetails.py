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

def GetInfo(index_nan):
    os.system('tshark -r logfile.pcap > raw_data.txt')
    filepath = "./raw_data.txt"
    file = open(filepath, "r")
    raw_data = file.read()
    raw_data = raw_data.split("\n")
    raw_data.pop()
    
    # remove nan rows
    for i in sorted(index_nan, reverse=True):
        del raw_data[i]
    # loop through

    return(raw_data)

