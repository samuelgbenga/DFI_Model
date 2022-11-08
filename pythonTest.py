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


pickled_model = pickle.load(open('dfimode2.pkl', 'rb'))

path = "./logfile.csv"
df = pd.read_csv(path)


df = df.dropna('columns')
df_new = df.rename(columns={'ip.proto': 'protocol_type', 'ip.flags':'flag', 'ip.len':'src_bytes',
                            'ip.frag_offset':'wrong_fragment', 'ip.flags.mf':'num_failed_logins',
                            'ip.flags.df':'logged_in', 'ip.flags.rb':'su_attempted', 'ip.checksum':'count', 
                            'frame.len':'dst_host_count', 'ip.dsfield':'dst_host_srv_count',
                            'ip.dsfield.dscp':'dst_host_diff_srv_rate',
                            'ip.dsfield.ecn':'dst_host_srv_diff_host_rate'})




# convert hex to decimal
# for flag, count
df_new['flag'] = df_new['flag'].apply(int, base=16)
df_new['count'] = df_new['count'].apply(int, base=16)

df_new['dst_host_srv_count'] = df_new['dst_host_srv_count'].apply(int, base=16)



# =============================================================================
# #mask = True
# #df_new.loc[df_new['flag'] > 22000, 'Fee'] = 15000
# #int("0xff", 0)
# 
# #for col in df_new['protocol_type']:
# #    print(int(col, 0))
# #for col in df.columns:
# #    print(col)
# =============================================================================

result = []
try:
   result = pickled_model.predict(df_new) 
except:
  print("There is an error in the data provided")
  

# =============================================================================
# #getDetails()
# #getDetails.RunCode(1)
# # protocol_type feature mapping
# # protocol_type feature mapping
# 
# # create a dictionary e.g {'normal': [ele, elem2], ....}
# 
# # for idx, elem in enumerate(result):
# #     dicts[idx, elem]= getDetails.RunCode(idx)
#     #print( idx,"",elem)
# #print(dicts.values())
#   
# #print(list(dicts)[0])
# #print(list(dicts.values())[0])
# #for elem in list(dicts.values())[0]:
# #    print(elem)
#    
# #output using pandas dataframe
# 
# 
# # for idx, elem in enumerate(packet_info):
# #     print(elem, end="")
# #     print("\t", result[idx])
# #     print()
# 
# # df_result = pd.DataFrame({'Name': packet_info, 'Price': result})
# =============================================================================


# working on the table output of the design commandline interface
def Gen_table():    
    packet_info = getDetails2.GetInfo();
    my_table = PrettyTable()
    
    my_table.add_column("Packet Information", packet_info)
    my_table.add_column("Attack Type", result)
    my_table.align = "l";
    
    #print(my_table) 
    return my_table

# print(df_result)
#print(packet_info)


































    





















   
    

    









