# -*- coding: utf-8 -*-
"""
Created on Mon May 09 16:20:27 2016

@author: liabbott
"""

import os
import sys
import pandas as pd

def find_consensus(df):
    
    profile = df.apply(pd.value_counts)
    profile.fillna(0, inplace=True)
    
    consensus = ''.join(profile.idxmax())
    
    return profile, consensus
    

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
        
    df = pd.DataFrame(df_dict).transpose()
    
    profile, consensus = find_consensus(df)
    
    out_path = os.path.join(os.getcwd(), 'output', 'CONS_output.txt')
    with open(out_path, 'wb') as f:
        f.write(consensus + '\n')
        for i in ['A', 'C', 'G', 'T']:
            row = [str(int(x)) for x in profile.loc[i, :]]
            if i == 'T':
                f.write(i + ': ' + ' '.join(row))
            else:
                f.write(i + ': ' + ' '.join(row) + '\n')


if __name__ == '__main__':
    main()