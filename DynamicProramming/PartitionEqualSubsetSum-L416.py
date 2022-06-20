'''
subsets sum should be same
sub_sum = totalSum/2 because we are creating two subsets with equal sum

so basically you need to find whether you are able to create subset whose sum is equal to totalSum/2. Hence you have two option at every step whether to consider or notconsider particular element in subset or not. 
From here onwards it's DP problem

Point to Note:
 if just target used as a key then also below memoisation code works with lesser space. But prblem is if we do notconsider part first then it will fail. 
 Using key as combination of target and curr_index is ideal way because at any particular (index,target) state we can't declare that state value just based on previous memo[target] value because from curr_index it might be possible to achieve that target if we explore further.



'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        curr_index = 0
        
        #memoisation
        memo={}
        
        if totalSum%2:
            return False
        #print(totalSum//2)
        ans= self.DP_canPartition(nums,totalSum//2,curr_index,memo)
        #print(len(memo))
        
        return ans
    
    def DP_canPartition(self,nums,target,curr_index,memo):
        
        if target == 0:
            return True
        if curr_index >= len(nums):
            return False
        
        key = str(target)+'-'+str(curr_index)
        if key in memo:
            return memo[key]
        
        consider,notconsider = False,False
        
        if target >= nums[curr_index]:
            consider = self.DP_canPartition(nums,target-nums[curr_index],curr_index+1,memo)
            
            ## if consider is true then you can directly return as we know atleast one solution is possible.
            if consider:
                memo[key] = consider
                return True
        
        notconsider = self.DP_canPartition(nums,target,curr_index+1,memo)
        
        memo[key] = notconsider
        
        return memo[key]
        
        
