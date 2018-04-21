#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    ct =0
    for i in range(0,n):
        for j in range(0,n):
            cka = a[j] % a[i]
            if cka == 0:
                ct += 1
    ct=round(ct/2)
    
    ctb = 0
    for i in range(0,m):
        for j in range(0,m):
            ckb = b[j] % b[i]
            if ckb == 0:
                ctb += 1
    ctb=round(ctb/2)
    c=ct+ctb
            
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
    
    
    
