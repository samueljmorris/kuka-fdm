# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:08:35 2019

@author: Rez
"""

import telnetlib
import sys

tn = telnetlib.Telnet('192.168.1.112', 23)
tn.read_until(b"Smoothie command shell")
str1 = str(sys.argv[1])
str2 = "G1 E" + str1 + "\n"
str3 = str2.encode('utf-8')
tn.write(str3)
tn.read_until(b"ok")
tn.write(b"exit")
tn.close
exit

