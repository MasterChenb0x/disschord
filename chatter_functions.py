#!/usr/local/bin/python3

import random
import sys
import time
import os

XA = int(round(time.time()))
XB = 243624362436
XC = random.getrandbits(12)
XD = os.getpgid(0)


# The following function was developed from an idea put forth by 
# George Marsaglia.  It is used for all the dice rolls.  From Wikipedia:
#
# Xorshift generators are among the fastest non-cryptographic random number generators requiring minimal code and state. 
# Although they do not pass every statistical test without further refinement, this weakness is well-known and easily amended 
# by combining them with a non-linear function, resulting e.g. in a xorshift+ or xorshift* generator. 
# A naive C implementation of a xorshift+ generator that passes all tests from the BigCrush suite (with an order of magnitude 
# fewer failures than Mersenne Twister or WELL) typically takes fewer than 10 clock cycles on x86 to generate a random number thanks to instruction pipelining.
#
# The following implementation was refined by bgm <~~ and 100% borrowed by MasterChen:
def xOrShift():
    global XA, XB, XC, XD
    e = (XA ^ (XA << 11)) & 0xFFFFFFFFFFFFFFFF
    XA = XB + XA
    XB = XC + XC
    XC = XD + XB
    XD = ((XA ^ (XD >> 19)) ^ (e ^ (e >> 8))) & 0xFFFFFFFFFFFFFFFF
    return XD
# End xOrShift

print(xOrShift())
