#!/bin/python3

import sys
import fractions

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
gcds = []
if n==1:
    print(a[0]+1)
else:
    for i in range(n):
        ans = 0
        for j in range(n):
            if j==i:
                continue
            else:
                ans = fractions.gcd(ans,a[j])
        gcds.append(ans)
    for k in range(len(gcds)):
        c = gcds.count(gcds[k])
        '''if c > 1:
            indexes = [l for l,val in enumerate(gcds) if val==gcds[k]]
            for g in range(len(indexes)):
                del gcds[indexes[g]]
            print(gcds[0])
            break
        else:
            print(gcds[k])'''
        if c == 1:
            print(gcds[k])
