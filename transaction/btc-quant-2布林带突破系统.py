""" 
Created on Sat Jan 14 14:33:26 2017 
 
@author: yunjinqi 
 
E-mail:yunjinqi@qq.com 
 
Differentiate yourself in the world from anyone else. 
"""  
#######################################################���ִ�ͻ�Ʋ���  
#ԭ��ͻ��95�վ��ߣ�����Ϊ2�Ĳ��ִ����������۸����34�վ��ߵ�ʱ���볡  
######################################################������Ӧģ��  
from OkcoinSpotAPI import *  
import pandas as pd  
import numpy as np  
import datetime  
import time  
#####################################################��ʼ����  
okcoinRESTURL = 'www.okcoin.cn'    
apikey='a3c363bd-28c7-4f6d-a04d-ac4a58e929b9'  
secretkey='83782FBD5E365EFC511EC739C0B54103'  
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)  
#####################################################�������ִ����ƶ�ƽ����ָ��  
def bbands_MA(M,N):  
    m=str(M)  
    n=str(N)  
    try:  
        kline=pd.DataFrame(okcoinSpot.getKline('1min',m,'0'))  
    except ValueError as e:  
        print('json����')  
    mid=kline.iloc[::,4].mean()  
    std=kline.iloc[::,4].std()  
    upper=mid+N*std  
    lower=mid-N*std  
    ma=kline.iloc[::,4].mean()  
    result=[upper,mid,lower]  
    return result  
######################################################����  
try:  
      ref_boll=bbands(94,2)  
      ref_upper=boll[0]  
      ref_lower=boll[2]    
      ref_close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
except:  
      print('json����')  
        
time.sleep(58)  
while True:  
    try:  
      boll=bbands(94,2)  
      upper=boll[0]  
      lower=boll[2]    
      close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
    except:  
      print('json����')  
      continue  
    if close>upper and ref_close<ref_upper:  
      print('�����ź�',okcoinSpot.trade('btc_cny','buy','7500','0.01'))  
    if close<ma34 and ref_close>ref_ma34:  
      print('�����ź�',okcoinSpot.trade('btc_cny','sell','1','0.01'))  
      
    try:  
      ref_boll=bbands(94,2)  
      ref_upper=boll[0]  
      ref_lower=boll[2]    
      ref_close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
    except:  
      print('json����')  
      continue  
    time.sleep(58)  
    now=datetime.datetime.now()  
    now=now.strftime('%Y-%m-%d %H:%M:%S')   
    i=i+1  
    print(now,i)