#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:42:21 2022

@author: samuel
"""
import os

def Capture_DFI():
    
    os.system("""tshark -w logfile.pcap -c 10 -T fields -E header=y -E separator=, -E occurrence=f -e ip.proto -e ip.flags -e ip.frag_offset -e ip.flags.mf -e ip.flags.df -e ip.flags.rb -e ip.checksum -e ip.dsfield -e ip.dsfield.dscp -e ip.dsfield.ecn  -e frame.len -e ip.len > logfile.csv""")



def Capture_DPI():
    os.system("""tshark -w dpi_packet.pcap -c 5""")