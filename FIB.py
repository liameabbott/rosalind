# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:15:44 2016

@author: Liam
"""

import os
import sys

def find_n_pairs(n, k):
    
    current = (1, 1)
                
    for i in range(2, n):
        two_ago = current[0]
        one_ago = current[1]
        new_ones = two_ago * k
        current = (one_ago, one_ago + new_ones)
        
    return str(current[1])


def main():
    
    data = sys.stdin.read()
    
    n, k = int(data.split()[0]), int(data.split()[1])    

    output = find_n_pairs(n, k)
    
    filename = 'FIB_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(output)


if __name__ == '__main__':
    main()