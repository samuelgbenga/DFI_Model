#python

import pandas as pd
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
import getDetails2

from prettytable import PrettyTable
#from texttable import Texttable

# stop warning
warnings.filterwarnings("ignore")

# loading ml engine using pickle
def Load_pickle():
    pickled_model = pickle.load(open('dfimode2.pkl', 'rb'))
    return pickled_model

def Get_result():
    try:
        path = "./logfile.csv"
        df = pd.read_csv(path)
    except:
        print("unable to load dataset")
    
    
    
    #df = df.dropna('columns')
    
    df_new = df.rename(columns={'ip.proto': 'protocol_type', 'ip.flags':'flag', 'ip.len':'src_bytes',
                                'ip.frag_offset':'wrong_fragment', 'ip.flags.mf':'num_failed_logins',
                                'ip.flags.df':'logged_in', 'ip.flags.rb':'su_attempted', 'ip.checksum':'count', 
                                'frame.len':'dst_host_count', 'ip.dsfield':'dst_host_srv_count',
                                'ip.dsfield.dscp':'dst_host_diff_srv_rate',
                                'ip.dsfield.ecn':'dst_host_srv_diff_host_rate'})
    
    df_new.fillna("nan", inplace=True)
    index_nan = df_new[df_new['flag'] == 'nan'].index
    
    df_new.drop(index_nan, inplace=True)
    
    
    
    
    # convert hex to decimal
    # for flag, count
    #df_new['flag'] = df_new['flag'].apply(int, base=16)
    try:
        df_new['flag'] = df_new['flag'].apply(Clean)
        df_new['count'] = df_new['count'].apply(Clean)
        
        df_new['dst_host_srv_count'] = df_new['dst_host_srv_count'].apply(Clean)
        # print(df_new)
        # print(index_nan)
        
    except:    
        print(df_new)
        
    #get pickled machine engine using
    pickled_model = Load_pickle()    
    result = []
    try:
       result = pickled_model.predict(df_new) 
    except:
      print("There is an error in the data provided")
      
     
    return result, index_nan
  

# clean the hex datas to integer
def Clean(x):
    i = int(x, 16)
    return i




def Gen_table():
    result, index_nan = Get_result()    
    packet_info = getDetails2.GetInfo(index_nan);
    my_table = PrettyTable()
    
    my_table.add_column("Packet Information", packet_info)
    my_table.add_column("Attack Type", result)
    my_table.align = "l";
    
    #print(my_table) 
    return my_table

#Gen_table()
# print(df_result)
#print(packet_info)


































    





















   
    

    









