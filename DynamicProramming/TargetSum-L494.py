'''
Classic DP problem for 0-1 knapsack.

At each index or point we have two options: to add positive sign or negative sign to currect value and go further to see if we can able to get target value.

'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index= 0
        memo={}
        return self.DP_findTargetSumWays(nums,index,target,memo)
    
    def DP_findTargetSumWays(self,nums,index,target,memo):
        
        totalWays = 0
        
        if target == 0 and  index == len(nums):
            return 1
        
        if index >=len(nums):
            return 0
        
        key = str(index)+'-'+ str(target)
        
        if key in memo:
            return memo[key]
        
        #if positive sign added then target sum reduced
        posSign = self.DP_findTargetSumWays(nums,index+1,target-nums[index],memo)
        
        # if negative sign added then target sum will increases
        negSign = self.DP_findTargetSumWays(nums,index+1,target+nums[index],memo)
        
        
        memo[key] = posSign + negSign
        
        return memo[key]
        
        
        
