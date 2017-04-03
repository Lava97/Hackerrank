#!/bin/python3

import sys


T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    # your code goes here
    bribe = 0
    for i in range(1, n+1):
        pos = q.index(i)
        if i - pos > 3:
            print("Too chaotic")
            break
        for j in range(pos):
            if(q[j]>i):
                bribe =  bribe + 1
    else:
        print(bribe)
