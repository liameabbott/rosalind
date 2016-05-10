# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:03:45 2016

@author: Liam
"""

import os
import sys
import RNACodonTable as rct


def get_protein_string(rna_string):
    
    n = len(rna_string)
    
    table = rct.RNACodonTable()

    protein_string = ''    
    for i in range(0, n, 3):
        substring = rna_string[i:(i+3)]
        protein = table.get_protein(substring)
        protein_string += protein
        
    return protein_string
    

def main():
    
    data = sys.stdin.readlines()[0].strip()
    
    output = get_protein_string(data)
    
    filename = 'PROT_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(str(output))
    

if __name__ == '__main__':
    main()