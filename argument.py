#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 01:52:05 2022

@author: samuel
"""

import sys
import os

# Python program to demonstrate
# command line arguments
 
# import argparse
# import os
 
# msg = os.system("./ndpi/ndpiReader -i dpi_packet.pcap")
 
# Initialize parser
# parser = argparse.ArgumentParser(prog = 'DPI_DFI' , description = msg, epilog = 'Text at the bottom of help')
# parser.parse_args()

# # parser.add_argument('-c', '--count')
# # args = parser.parse_args()
# print(args.count)

# 'import pandas as pd

# path = "./dpi_file.csv"
# df = pd.read_csv(path)
# '



# n = int(sys.argv[1])

# print(n+2)


try:
    
    manual = """
-D -> Display the available interface
-cp -> number of packet to capture for dpi. Default is 5
-cf -> number of packet to capure for dfi. Default is 30  
"""
    
    if len(sys.argv) == 1:
        print("\n-h, --help ->  displays description or help")
        
        help_desc ="""
************************************************************
*                                                          *
*    ->THIS IS A PACKET DPI_DFI PACKET INSPECTION<-        *
*                                                          *
************************************************************
    """
       
       
        help_last = """\nThe program will display an the help or Description 
of the system if no argument is passed\n
                    """
    
    
        print(help_desc)
        print(manual)
        print(help_last)
        
        
    if len(sys.argv) > 1:
        n = str(sys.argv[1])
        
        if n == "-D":
            the_string = """tshark {}""".format(n)
    
            os.system(the_string)
            
        elif n == "-c":
            m = int(sys.argv[2])
            
            the_string = """tshark {} {}""".format(n, m)
            
            os.system(the_string)
        elif n == "-h" or n == "--help":
            print(manual)
            
        else:
            print("something went wrong argument")
        
    
except: 
    print("an exceptiong was encountered")
    
# write the help first statement first
# for now so user can choose prefered interface















