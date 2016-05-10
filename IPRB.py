# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:29:02 2016

@author: Liam
"""

import os
import sys


def findProbabilityDomPheno(n_dom, n_het, n_rec):
    
    tot = float(n_dom + n_het + n_rec)  
    
    p_2d = (n_dom/tot * (n_dom-1)/(tot-1)) * 1.00
    p_2h = (n_het/tot * (n_het-1)/(tot-1)) * 0.75
    p_2r = (n_rec/tot * (n_rec-1)/(tot-1)) * 0.00
    
    p_1d1h = (n_dom/tot * n_het/(tot-1) + n_het/tot * n_dom/(tot-1)) * 1.00
    p_1r1h = (n_rec/tot * n_het/(tot-1) + n_het/tot * n_rec/(tot-1)) * 0.50
    p_1d1r = (n_dom/tot * n_rec/(tot-1) + n_rec/tot * n_dom/(tot-1)) * 1.00
    
    probs = [p_2d, p_2h, p_2r, p_1d1h, p_1r1h, p_1d1r]
    
    return sum(probs)


def main():
    
    data = [float(x) for x in sys.stdin.read().split()]
    
    k, m, n = data
    
    output = findProbabilityDomPheno(k, m, n)
    
    filename = 'IPRB_output.txt'
    file_path = os.path.join(os.getcwd(), 'output', filename)
    with open(file_path, 'wb') as f:
        f.write(str(output))
    

if __name__ == '__main__':
    main()