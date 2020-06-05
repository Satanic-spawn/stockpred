#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:22:50 2020

@author: satansspawn
"""
#sy = "RELIANCE.NS"
#key = 'OAPX1MWCR5GSEPXK'

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import trial
import os
import test



# setting the windows size
# declaring string variable
# for storing name and password


#s = input("Enter stock symbol:")
#kk = input("Enter your API key for Alpha Vantage:")
print("Select timeframe from menu:")
print("1. 60 min")
print("2. 30 min")
print("3. 15 min")
print("4. 5 min")
print("5. 1 min")
print("6. Day adjusted")
print("7. Week adjusted")
print("8. Month adjusted")
print("9. Predict model for month close using week")


ch = int(input())

if ch == 1:
    trial.og60(s, kk)
if ch == 2:
    trial.og30(s, kk)
if ch == 3:
    trial.og15(s, kk)
if ch == 4:
    trial.og5(s, kk)
if ch == 5:
    trial.og1(s, kk)
if ch == 6:
    trial.ogdaily(s, kk)
if ch == 7:
    trial.ogweekly(s, kk)
if ch == 8:
    trial.ogmonthly(s, kk)
if ch == 9:
    test.st(s, kk)

#print(ch)





root.mainloop()
"""trial.og60(s, kk)
trial.og30(s, kk)
trial.og15(s, kk)
trial.og5(s, kk)
trial.og1(s, kk)
trial.ogdaily(s, kk)
trial.ogweekly(s, kk)
trial.ogmonthly(s, kk)"""
