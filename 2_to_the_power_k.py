# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:47:45 2022

@author: Aurko
"""

class Solution:
# @param A : string
# @return an integer
    
    def __init__(self):
        self.A = "A: \"1\""
        
    def power(self, A):
        num = A.split(":")[1].strip(' " ')
        #num = int(num)
        #num = 12132343242325435
        numList = list(map(int, str(num)))
        print(numList)
        
        ans = 0
        
        for i in range(numList):
            x = int(numList[i])
            if(x % 2 != 0):
                ans = 0
                
        return ans
        #while num != 0:
        #    x = num % 2
        #    if(x != 0):
        #        num = num / 2
        #    else:
        #        ans = 0
        
        #if(num > 1):
        #    if (math.log(num, 2)).is_integer():
        #        ans = 1
        #    else:
        #        ans = 0
        #else:
        #    ans = 0
        #return ans
    
A = input()
x = Solution()
print(x.power(A))
   