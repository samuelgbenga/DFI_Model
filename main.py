#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 02:56:47 2022

@author: samuel
"""

import os
import subprocess


import multiprocessing
import time
import tsharkcmd
import dfi_module
import dpi_module
import sys
import warnings



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
        time.sleep(1) 
            
          
          
           
          
#run the program
def Run_main():
    if __name__ == '__main__':
        p = Process(0)
        p.start()
        p = Process(1)
        p.start()
        p.join()
        

# continue the program manually
def Continue_exec():
    while (True):
        
        
        x = str(input("continue to capture (yes/no) "))
        if x == "yes":
            Run_main()
        elif x == "no":
            break
        else:
            print("you entered a wrong input value: ", x)
            break



# how to contiue inspection until https is captured completely

# program execution center
# supply arguments 

# this function returns argument name
# supplied to the dpi and dfi


# Main execution argument passing

def Main_execution():
    
    try:
        
        manual = """
    -D          -> Display the available interface
    -cp         -> number of packet to capture for dpi. Default is 5
    -cf         -> number of packet to capure for dfi. Default is 30  
    -r, --run   -> run the program or start inspection
                   This will run the program with the default interface
    -i          -> this is used to specify the interface
    -h, --help  ->  displays description or help
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
                    
            elif n == "--run" or n == "-r":
                Run_main()
                Continue_exec()
                
            else:
                
                print("something went wrong argument")
        
    except: 
        print("an exceptiong was encountered")
        
# The dpi and dfi functions

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

Main_execution()


# def Testing(x):
#     if x == 1:
#         print("yes")
#     elif x == 2:
#         print("no")

#Run_main()
#Continue_exec()














