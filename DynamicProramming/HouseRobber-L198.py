'''
Robber have two option at each house: Rob or Don'tRob
Depending on this it will either rob next house or skip next house.
Using Dynmic approach we can solve this problem. If robber decide to rob current house
add amount to final value and return max amount at final

TC: O(n) with memoization
SC: O(n) max recursive call stack or max memo dictionary size.

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        currentHouse = 0
        memo = {}
        return self.maxAmountRobbed(currentHouse, nums,memo)
    
    def maxAmountRobbed(self,currentHouse:int, nums: List[int], memo:dict)->int:
        
        if currentHouse >= len(nums):
            return 0
        
        if currentHouse in memo:
            return memo[currentHouse]
        
        rob = nums[currentHouse]+self.maxAmountRobbed(currentHouse+2,nums,memo)
        notRob =  self.maxAmountRobbed(currentHouse+1,nums,memo)
        
        memo[currentHouse] = max(rob,notRob)
        
        return memo[currentHouse]
