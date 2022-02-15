'''
My solution to the Hackerrank challenge "Birthday cake candles", avaiable in https://www.hackerrank.com/challenges/birthday-cake-candles/problem 
All data regarding the challenge can be found in the link above.
'''

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    i=0
    max=1
    for i in range (len(candles)-1):
        if candles[i]==candles[i+1]:
            i+=1
            max+=1
        else:
            break
    return max

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')