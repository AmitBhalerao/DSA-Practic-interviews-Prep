'''
    Points to remember:
    This is same as original house robber. Only difference is house here are in circle. Now in order to get maxsum value and avoid considering first and last adjacant house into final sum, problem is divided into two arrays. One without first house and 2nd without last house. 
    so we will get two max values for above mentioned two array and max of those values will be our final answer. 
    '''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        memo1={}
        max1 = self.maxAmountRobbed(0,nums[:-1],memo1)
        memo2={}
        #note that for 2nd call currentHouse=0 is passed as it is respective to the nums array passed
        max2 = self.maxAmountRobbed(0,nums[1:],memo2)
        
        return max(max1,max2)
    
    
    def maxAmountRobbed(self,currentHouse:int, nums: List[int], memo:dict)->int:
        #print("nums: {} currentHouse: {} memo:{}".format(nums,currentHouse,memo))
        if currentHouse >= len(nums):
            return 0
        
        if currentHouse in memo:
            return memo[currentHouse]
        
        rob = nums[currentHouse]+self.maxAmountRobbed(currentHouse+2,nums,memo)
        notRob =  self.maxAmountRobbed(currentHouse+1,nums,memo)
        
        memo[currentHouse] = max(rob,notRob)
        
        
        return memo[currentHouse]
