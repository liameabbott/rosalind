# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:55:22 2016

@author: Liam
"""

import os
import sys
import pandas as pd


def common_substring(df):
    
    n, m = df.shape
    
    list_strings = [''.join(df.iloc[i,:].dropna()) for i in xrange(n)]
    list_strings.sort(key=len)    
    
    shortest = len(list_strings[0])
    max_length = shortest
    
    while max_length > 0:
        
        for i in xrange(shortest - max_length):
            
            proposed = list_strings[0][i:(i+max_length)]
            
            for j in xrange(1, n):
                
                if proposed not in list_strings[j]:
                    break
                
                if j == (n-1):
                    return proposed
        
        max_length -= 1
        
    return ''
            

def main():

    data = sys.stdin.readlines()

    n = len(data)

    df_dict = {}
    for i in xrange(n):
        row = data[i].strip()
        if row[0] == '>':
            key = row[1:]
            df_dict[key] = []
            continue
        df_dict[key] += list(row)
    df_dict = {k: pd.Series(v) for k, v in df_dict.iteritems()}
        
    df = pd.DataFrame(df_dict).transpose()
    
    cs = common_substring(df)
    
    out_path = os.path.join(os.getcwd(), 'output', 'LCSM_output.txt')
    with open(out_path, 'wb') as f:
        f.write(cs)
    
    
if __name__ == '__main__':
    main()