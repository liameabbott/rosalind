# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:08:19 2016

@author: Liam
"""

import os
import sys

def HammingDistance(string1, string2):
    
    n1 = len(string1)
    n2 = len(string2)
    n_min = min(n1, n2)
    if n1 == n2:
        distance = 0
    else:
        distance = max([n1, n2]) - n_min
    for i in range(n_min):
        if string1[i] != string2[i]:
            distance += 1
            
    return distance


def main():
    
    data = sys.stdin.readlines()
        
    string1 = data[0].strip()
    string2 = data[1].strip()
    
    output = HammingDistance(string1, string2)
    
    filename = 'HAMM_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(str(output))
    
    
if __name__ == '__main__':
    main()