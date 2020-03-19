# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:44:12 2019
"""

import datetime
import urllib.request
import json
import pandas as pd

doviz = pd.DataFrame(columns=["date","name","open","close","high","low","volume","isCurrency"])




time_ = []
close_ = []
open_ = []
high_ = []
low_ = []
target_ = []
change_ = []


baslangic = "20170723"
bitis = "20190723"

####### Döviz için ########

names = ["SUSD","SEUR","SGBP","SCHF"]


print("- Part I -")

for i in names:
    
    time_ = []
    close_ = []
    open_ = []
    high_ = []
    low_ = []
    
    temp_frame = pd.DataFrame(columns=['date','name','open','close','high','low','volume','isCurrency'])
    name = i
    
    temp_val = "https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&exchange=FREE&name="+name+"&market=N&last=500&period=1440&from="+baslangic+"000000&to="+bitis+"000000"
    with urllib.request.urlopen(temp_val) as url:
        data = json.loads(url.read().decode())
    
    data = data["dataSet"]
    
    print(i," collecting data...",end="")
    for j in data:
        previous = float(j["close"])
        date_ = str(j["date"])[:10]
        time_.append(datetime.datetime.fromtimestamp(int(date_)).strftime('%Y-%m-%d'))
        close_.append(j["close"])
        open_.append(j["open"])
        high_.append(j["high"])
        low_.append(j["low"])
        
    temp_frame = pd.DataFrame(columns=['date','name','open','close','high','low','volume','isCurrency'])
    temp_frame["date"] = time_
    temp_frame["name"] = name
    temp_frame["open"] = open_
    temp_frame["close"] = close_
    temp_frame["high"] = high_
    temp_frame["low"] = low_
    temp_frame["volume"] = None
    temp_frame["isCurrency"] = 1
    doviz = doviz.append(temp_frame,ignore_index=True)
    print(" ",i," is collected")



####### Hisse için ########
print("- Part II -")


names = ["ADEL","GLBMD","BURVA","VAKBN","GARAN","HALKB","ALARK","KOZAA","PETKM","SNGYO","ZOREN",
         "ISCTR","IHEVA","BURCE","YYAPI","TGSAS","FONET","BIZIM","EUYO","SANKO","MTRYO","GEREL"]



for i in names:
    time_ = []
    close_ = []
    open_ = []
    high_ = []
    low_ = []
    volume_ = []
    temp_frame = pd.DataFrame(columns=['date','name','open','close','high','low','volume'])
    
    print(i," collecting data...",end="")
    
    name = i
    temp_val = "https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&exchange=BIST&name="+name+"&market=E&group=E&last=500&period=1440&from="+baslangic+"000000&to="+bitis+"000000"
    with urllib.request.urlopen(temp_val) as url:
        data = json.loads(url.read().decode())
    
    data = data["dataSet"]
    
    for j in data:
        date_ = str(j["date"])[:10]
        time_.append(datetime.datetime.fromtimestamp(int(date_)).strftime('%Y-%m-%d'))
        close_.append(j["close"])
        open_.append(j["open"])
        high_.append(j["high"])
        low_.append(j["low"])
        volume_.append(j["volume"])
        
    
    temp_frame["date"] = time_
    temp_frame["name"] = name
    temp_frame["open"] = open_
    temp_frame["close"] = close_
    temp_frame["high"] = high_
    temp_frame["low"] = low_
    temp_frame["volume"] = volume_
    temp_frame["isCurrency"] = 0
    doviz = doviz.append(temp_frame,ignore_index=True)
    print(" ",i," is collected")


doviz.to_excel("PATH")
