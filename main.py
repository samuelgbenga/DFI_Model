#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 02:56:47 2022

@author: samuel
"""

import os
import subprocess
import dfi_module
#import reload

# 'os.system("""tshark -c 5""")

# proc1 = subprocess.call('tshark -c 10', shell=True)
# print("hello world")'

import multiprocessing
import time
import tsharkcmd
import dfi_module

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        #print("I'm the process with id: {}".format(self.id))
        if self.id == 0:
            DPI_func()
            
        if self.id == 1:
            DFI_func()
        
        
#reload(dfi_module)

# DPI function 
def DPI_func():
    #os.system("""tshark -w dpi_packet.pcap -c 5""")
    tsharkcmd.Capture_DPI()
        
    
# DFI_ function 
def DFI_func():
    tsharkcmd.Capture_DFI()
    dfi_table = dfi_module.Gen_table()
    #dfi = dfi_module.Gen_table()
    print(dfi_table)
    


# run the program
if __name__ == '__main__':
    p = Process(0)
    p.start()
    p = Process(1)
    p.start()
    p.join()
    


    
    
    




















