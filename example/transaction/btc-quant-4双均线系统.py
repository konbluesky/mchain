# -*- coding: utf-8 -*-  
""" 
Created on Fri Jan 13 23:47:40 2017 
 
@author: yunjinqi 
 
E-mail:yunjinqi@qq.com 
 
Differentiate yourself in the world from anyone else. 
"""  
####################################����ģ��  
  
  
from OkcoinSpotAPI import *  
import pandas as pd  
import numpy as np  
import datetime  
import time  
  
  
###################################��ʼ����  
okcoinRESTURL = 'www.okcoin.cn'    
apikey='978e1f34-acf5-40d1-b49e-f8b80618fd35'  
secretkey='79CCAADA3C40F24FB7B01E83763818E6'  
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)  
##################################��ȡ��������  
okcoinSpot.userinfo()  
###okcoinSpot.getKline('1min','14','1'))#��ȡK������  
#ma8=pd.DataFrame(okcoinSpot.getKline('1min','8','0')).ix[::,4].mean()  
#ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).ix[::,4].mean()  
try:  
    ref_ma8=pd.DataFrame(okcoinSpot.getKline('1min','8','0')).ix[::,4].mean()  
    ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).ix[::,4].mean()  
    print('ref_ma8:',ref_ma8,'����ref_ma34',ref_ma34)  
except ValueError as e:  
    print('json����')  
time.sleep(58)  
i=0  
while True:  
       try:  
           ma8=pd.DataFrame(okcoinSpot.getKline('1min','8','0')).ix[::,4].mean()  
           ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).ix[::,4].mean()  
           print('ma8:',ma8,'����ma34',ma34)  
       except ValueError as e:  
           print('json����')  
           continue  
       if ma8>ma34 and ref_ma8<=ref_ma34:  
           print('�����ź�',okcoinSpot.trade('btc_cny','buy','7500','0.01'))  
       if ma8<ma34 and ref_ma8>=ref_ma34:  
           print('�����ź�',okcoinSpot.trade('btc_cny','sell','1','0.01'))  
       time.sleep(58)  
       try:  
           ref_ma8=pd.DataFrame(okcoinSpot.getKline('1min','8','0')).ix[::,4].mean()  
           ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).ix[::,4].mean()  
           print('ref_ma8:',ref_ma8,'����ref_ma34',ref_ma34)  
       except ValueError as e:  
           print('json����')  
             
           continue  
       now=datetime.datetime.now()  
       now=now.strftime('%Y-%m-%d %H:%M:%S')   
       i=i+1  
       print(now,i)  