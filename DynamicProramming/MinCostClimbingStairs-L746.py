'''
Dynamic methods solution

TC: O(n) as max value for currentStair is n
SC: O(n) as max depth of stack with one step recursive function approach is n
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target = len(cost)
        memo={}
        start0 = self.minCost(0,target,cost,memo)
        start1 = self.minCost(1,target,cost,memo)
        
        return min(start0,start1)
    
    def minCost(self, currentStair : int, target : int, cost:List[int], memo:dict)->int:
        
        if currentStair == target:
            return 0
        if currentStair > target :
            return 1000
        if currentStair in memo:
            return memo[currentStair]
        
        oneStepCost = cost[currentStair]+self.minCost(currentStair+1,target,cost,memo)
        twoStepCost = cost[currentStair]+self.minCost(currentStair+2,target,cost,memo)
        
        memo[currentStair] = min(oneStepCost,twoStepCost)
        
        return memo[currentStair]
