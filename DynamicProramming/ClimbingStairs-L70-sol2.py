'''
TC: O(n)
SC: O(n)

This is fibonnacci series method only. Base conditions are added in order to calculate answers for the 3rd step onwards.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        s=[ 0 for _ in range(n+1)]
       
        
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n>2:
             
            s[1]=1
            s[2]=2
            for i in range(3,n+1):
                s[i] = s[i-1]+s[i-2]
        
        return s[n]
