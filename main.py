#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 02:56:47 2022

@author: samuel
"""

import os
import subprocess

os.system("""tshark -c 5""")

proc1 = subprocess.call('tshark -c 10', shell=True)
print("hello world")

