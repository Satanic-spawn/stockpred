#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:36:50 2020

@author: satansspawn
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import csv
import stockp
import pandas as pd
import trial
import pickle
import  numpy as np
import datetime

x = str(datetime.datetime.now())
x = x[:10]
#print(x)
ctrd = 4942
ctrw = 1051
dw = []
dm = []


def ogmonthly(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    #ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    global datam
    sym = name
    datam, meta_data = ts.get_monthly(symbol=sym)
    print("model for month of data")
    #print(data)
    fn = name+".month.csv"
    with open(fn, 'w') as ff:
        datam.to_csv(ff)
    #stockp.tr(fn)

def ogweekly(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    #ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    global dataw
    sym = name
    dataw, meta_data = ts.get_weekly(symbol=sym)
    print("model for week data")
    #print(data)
    fn = name+".week.csv"
    with open(fn, 'w') as ff:
        dataw.to_csv(ff)
    #stockp.tr(fn)

#ogmonthly("RELIANCE.NS", 'api key')
#ogweekly("RELIANCE.NS", 'api key')



def st(name, k):
    #ogmonthly(name, k)
    #ogweekly(name, k)
    fnw = name+".week.csv"
    fnm = name+".month.csv"
    dfw = pd.read_csv(fnw)[['date', '1. open', '2. high', '3. low', '5. volume']]
    #print(dfw.head())
    dfm = pd.read_csv(fnm)[['date', '1. open', '2. high', '3. low', '4. close', '5. volume']]
    with open('XYD.csv', 'w') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames = ['1. open', '2. high', '3. low', '5. volume', '6. close'])
        writer.writeheader()

    with open('XYD.csv', 'a') as outcsv:
        w = csv.writer(outcsv)
        for i in dfm.index:
            if dfm['date'][i] == x:
                continue
            c = str(dfm['4. close'][i])
            for j in dfw.index:
                if dfm['date'][i][:-2] == dfw['date'][j][:-2]:
                    row = dfw['1. open'][j], dfw['2. high'][j], dfw['3. low'][j], dfw['5. volume'][j], c
                    #print(row)
                    w.writerow(row)
    stockp.trs('XYD.csv')
    clf = pickle.load(open("XYD.sav", "rb"))
    key = k
    ts = TimeSeries(key, output_format='pandas')
    #ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    global dataw
    sym = name
    dataw, meta_data = ts.get_intraday(symbol=sym,interval='60min', outputsize='full')
    with open("testdata.csv", "w") as cc:
        dataw.to_csv(cc)
    T = pd.read_csv("testdata.csv")
    xxx = T[['1. open', '2. high', '3. low', '5. volume']]
    ch1 = T[['1. open']]
    #print(clf.predict(xxx))
    #print(ch1)
    rise = 0
    fall = 0
    pdd = clf.predict(xxx)
    for i in ch1.index:
        if ch1["1. open"][i] > pdd[i]:
            fall += 1
        else:
            rise += 1


    if fall > rise:
        print("The stock will fall.")
        return "fall"
    else:
        print("The stock will rise.")
        return "rise"



#st("RELIANCE.NS", 'OAPX1MWCR5GSEPXK')
