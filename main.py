#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 02:56:47 2022

@author: samuel
"""

import os
import subprocess
#import reload

# 'os.system("""tshark -c 5""")

# proc1 = subprocess.call('tshark -c 10', shell=True)
# print("hello world")'

import multiprocessing
import time
import tsharkcmd
import dfi_module
import dpi_module
import sys
import warnings

#key interrupt function
# import sys, signal
# def signal_handler(signal, frame):
#     print("\nprogram exiting gracefully")
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)
#warnings.filterwarnings("ignore")

#Multiprocessing
class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        
        # processing dfi
        if self.id == 0: 
            DFI_func()
            
          #processing dpi   
        if self.id == 1:
            DPI_func()
        
#reload(dfi_module)

# DPI function 
def DPI_func():
    #os.system("""tshark -w dpi_packet.pcap -c 5""")
    tsharkcmd.Capture_DPI()
    dpi_module.Get_dpi()
    #print("working on it")
        
    
# DFI_ function 
def DFI_func():
    tsharkcmd.Capture_DFI()
    dfi_table = dfi_module.Gen_table()
    #dfi = dfi_module.Gen_table()
    print(dfi_table)
    

# DFI_func()
# DPI_func()

#run the program
def Run_main():
    if __name__ == '__main__':
        p = Process(0)
        p.start()
        p = Process(1)
        p.start()
        p.join()
        


# control with input
Run_main()
while (True):
    
    
    x = str(input("continue to caputure (yes/no) "))
    if x == "yes":
        Run_main()
    elif x == "no":
        break
    else:
        print("you entered a wrong input value: ", x)
        break



# how to contiue inspection until https is captured completely
    




















