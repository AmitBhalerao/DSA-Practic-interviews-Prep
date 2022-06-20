class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[x] = minimum number of steps to get x A on screen
        
        # maximum number of steps to get x A , is to get copy 1 A and paste it x-1 times - total x operations
        # so dp[x] = x to begin with
        dp = [ i for i in range(n+1)]
        # exception is 0 and 1, for which dp[0]=0 and dp[1]=0
        dp[0]=dp[1]=0
        
        # how to divide the number x?
        # x can be expressed as a*b
        # lets say b is always higher than a
        # so highest value of b can be x                : x is prime (x can not be divided)
        # or highest value of b can be some factor of x : x is not prime
        # 
        # if x is not prime, collect b As in clipboard and paste it a -1 (or x//b - 1) times - 
        # collecting b As in clipboard = dp[b] + 1 (get b As:dp[b] and then "copy":1 )
        # paste b As in (a-1) times    = a - 1 = x//b - 1
        #
        # so dp[x] = dp[b] + 1 + x//b - 1 ---- where b is largest factor of x
        
        for i in range(2,n+1):
            for j in range(i-1,1,-1):
                if ( i%j == 0 ):
                    dp[i] = dp[j] + 1 + i//j - 1
                    break
        
        return dp[n]
