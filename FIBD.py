# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:43:49 2016

@author: Liam
"""

import os
import sys


def fibonacci(n, m):
    
    generations = [1] + ([0] * (m-1))
    
    for i in xrange(n-1):
        new = [sum(generations[1:])]
        old = generations[:(m-1)]
        generations = new + old
        
    return sum(generations)


def main():
    
    data = sys.stdin.readline()
    n, m = [int(x.strip()) for x in data.split()]
    
    solution = fibonacci(n, m)
    
    out_path = os.path.join(os.getcwd(), 'output', 'FIBD_output.txt')
    with open(out_path, 'wb') as f:
        f.write(str(solution))


if __name__ == '__main__':
    main()