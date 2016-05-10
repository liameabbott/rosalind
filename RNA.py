# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:30:53 2016

@author: Liam
"""

import os
import sys
import pandas as pd

def transcribeDNA(dna):
    
    rna = dna.replace("T", "U")
    
    return rna


def main():
    
    data = sys.stdin.read()
    
    dna = data.strip()
    
    rna = transcribeDNA(dna)
    
    filename = 'RNA_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(rna)




if __name__ == '__main__':
    main()