#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:42:21 2022

@author: samuel
"""
import os

def Capture_DFI():
    
    os.system("""tshark -i 1 -c 25 -f "tcp dst port 443 or 8443" -w logfile.pcap -T fields -E header=y -E separator=, -E occurrence=f -e ip.proto -e ip.flags -e ip.frag_offset -e ip.flags.mf -e ip.flags.df -e ip.flags.rb -e ip.checksum -e ip.dsfield -e ip.dsfield.dscp -e ip.dsfield.ecn  -e frame.len -e ip.len > logfile.csv""")
   

def Capture_DPI():
    os.system("""tshark -i 1 -c 10 -f "tcp dst port 80 or 8080" -w dpi_packet.pcap""")

    
