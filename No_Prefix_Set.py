# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 08:39:51 2022

@author: Aurko
"""


#!/bin/python3
#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    pref = {}
    for w in words:
        pw = ''
        for l in w:
            pw += l
            if pw in pref and (pref[pw] or len(pw) == len(w)):
                print("BAD SET")
                print(w)
                return
            pref[pw] = len(pw) == len(w) or (False if not pw in pref else pref[pw])
        
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
