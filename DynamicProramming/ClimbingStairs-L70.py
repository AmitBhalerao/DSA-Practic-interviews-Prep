'''
TC: O(2^n) for Non-memoized code
TC: O(n) as currentStair max value can be n. For memoised solution
SC: O(n)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        def totalWaysToClimb(currentStair:int, target: int,memo:dict)->int:
            if currentStair == target:
                return 1
            if currentStair > target:
                return 0
            if currentStair in memo:
                return memo[currentStair]
            onestep = totalWaysToClimb(currentStair+1,n,memo)
            twostep = totalWaysToClimb(currentStair+2,n,memo)
            
            memo[currentStair] = onestep+twostep
            
            return memo[currentStair]
        
        memo = {}
        return totalWaysToClimb(0,n,memo)
