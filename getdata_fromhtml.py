# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

#path = 'StrataScratch.html'
def getdata_fromhtml(path):
    data = []
    # get the header from html file
    header_list = []
    soup = BeautifulSoup(open(path), 'html.parser')
    header = soup.find_all('table')[0].find('tr')
    
    for item in header:        
        try:
            header_list.append(item.get_text())
        except:
            continue        
 
    # Get the data
    html_data = soup.find_all('table')[0].find_all('tr')[1:]
    for item in html_data:
        sub_data = []
        for sub_item in item:
            try:
                sub_data.append(sub_item.get_text())
            except:
                continue
        data.append(sub_data)
    # Store the data as a dataframe 
    df = pd.DataFrame(data = data, columns= header_list)
    
    #save it as a csv
    #df.to_csv('/home/kassa/Data employee.csv', index=False)
    return df