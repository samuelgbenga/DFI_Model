#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:43:37 2022

@author: samuel
"""
import os
import subprocess





# capture and read file into dpi for result
def Get_dpi():
    os.system("./ndpi/ndpiReader -i dpi_packet.pcap")