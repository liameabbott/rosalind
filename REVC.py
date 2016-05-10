# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:30:53 2016

@author: Liam
"""

import os
import sys

def reverseComplement(dna):
    
    nuc_dict = {'A':'T',
                'T':'A',
                'C':'G',
                'G':'C'}
                
    reverse = dna[::-1]
    
    reverseComp = [nuc_dict[x] for x in reverse]
    
    return ''.join(reverseComp)


def main():
    
    data = sys.stdin.read()
    
    dna = data.strip()

    reverse_comp = reverseComplement(dna)
    
    filename = 'REVC_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(reverse_comp)


if __name__ == '__main__':
    main()