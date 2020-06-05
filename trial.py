#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:31:42 2020


@author: satansspawn
"""
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import stockp
import csv


def ogmonthly(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_monthly(symbol=sym)
    print("model for month of data")
    print(data)
    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)


def ogweekly(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_weekly(symbol=sym)
    print("model for week data")
    print(data)
    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)


def ogdaily(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_daily(symbol=sym, outputsize='full')
    print("model for day of data")
    print(data)
    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)


def og60(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='60min', outputsize='full')
    print("model for 60 min of data")

    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)

def og30(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='30min', outputsize='full')
    print("model for 30 min of data")

    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)

def og15(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='15min', outputsize='full')
    print("model for 15 min of data")

    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)

def og5(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    #sym = input('Enter stock symbol: ')
    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='5min', outputsize='full')
    print("model for 5 min of data")

    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)

def og1(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)

    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='1min', outputsize='full')
    print("model for 1 min of data")

    fn = name+".csv"
    with open(fn, 'w') as ff:
        data.to_csv(ff)
    stockp.tr(fn)

def og(name, k):
    key = k
    ts = TimeSeries(key, output_format='pandas')
    ti = TechIndicators(key)
    fn = name+".csv"


    sym = name
    data, meta_data = ts.get_intraday(symbol=sym,interval='60min', outputsize='full')
    #print("model for 15 min of data")

    with open(fn, 'w') as ff:
        data.to_csv(ff)
    #stockp.tr(fn)





#og("RELIANCE.NS", 'OAPX1MWCR5GSEPXK')
