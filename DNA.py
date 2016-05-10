# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:30:53 2016

@author: Liam
"""

import os
import sys
import pandas as pd

def countNucleotides(dna):
    
    df = pd.Series(list(dna))
    df = df.groupby(df.values).count()
    
    return [str(x) for x in df]


def main():
    
    data = sys.stdin.read()
    
    dna = data.strip()
    
    counts = countNucleotides(dna)
    
    filename = 'DNA_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(' '.join(counts))




if __name__ == '__main__':
    main()