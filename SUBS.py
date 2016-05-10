# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:45:08 2016

@author: Liam
"""


import os
import sys


def get_positions(string, substring):
    
    n_string = len(string)
    n_substring = len(substring)    
    
    positions = []
    
    for i in range(n_string - n_substring):
        
        test = string[i:(i+n_substring)]
        
        if test == substring:
            positions.append(i+1)
    
    return positions
    

def main():
    
    data = sys.stdin.readlines()
    
    string = data[0].strip()
    substring = data[1].strip()
    
    output = get_positions(string, substring)
    output = ' '.join([str(x) for x in output])
    
    filename = 'SUBS_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(str(output))
    

if __name__ == '__main__':
    main()