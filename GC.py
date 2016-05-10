# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:54:15 2016

@author: Liam
"""

import os
import sys
import pandas as pd

def find_gc_pct(string):
    
    mapper = {'G': 'yes',
              'C': 'yes',
              'A': 'no',
              'T': 'no'}
              
    map_srs = pd.Series(mapper)
    
    srs = pd.Series(list(string)).map(map_srs)
    
    srs = srs.groupby(srs.values).count()
    
    gc_pct = (float(srs['yes'])/sum(srs)) * 100
    
    return gc_pct


def main():
    
    data = sys.stdin.readlines()
    
    dna_dict = {}
    key = data[0][1:]
    value = ''
    for line in data[1:]:
        if line[0] == '>':
            dna_dict[key] = value            
            key = line[1:]
            value = ''
            continue
        value = value + line
    dna_dict[key] = value
    
    highest_dna = dna_dict.keys()[0]
    highest_pct = find_gc_pct(dna_dict[highest_dna])
    for dna in dna_dict:
        pct = find_gc_pct(dna_dict[dna])
        if pct > highest_pct:
            highest_dna = dna
            highest_pct = pct
    
    output = highest_dna + '\n' + str(highest_pct)
    
    filename = 'GC_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(output)


if __name__ == '__main__':
    main()