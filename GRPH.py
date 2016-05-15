# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:18:34 2016

@author: Liam
"""

import os
import sys
import pandas as pd


def graph(df):
    
    n, k_max = df.shape

    adj_list = []
    for i in xrange(n):
        s_name = df.index[i]
        s = ''.join(df.iloc[i,:].dropna())
        suffix = s[-3:]
        for j in xrange(n):
            t_name = df.index[j]
            t = ''.join(df.iloc[j, :].dropna())
            if s == t:
                continue
            prefix = t[:3]
            if suffix == prefix:
                adj_list.append(s_name + ' ' + t_name)
    
    return adj_list
            

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
    
    adj_list = graph(df)
    
    out_path = os.path.join(os.getcwd(), 'output', 'GRPH_output.txt')
    with open(out_path, 'wb') as f:
        f.write('\n'.join(adj_list))
    
    
if __name__ == '__main__':
    main()