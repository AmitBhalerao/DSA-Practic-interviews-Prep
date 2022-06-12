   '''
        excl_sum : max sum excluding current house robbery. For first house excl_sum = 0
        incl_sum : max sum including current house robbery. So this will be equal to
                  prev excl_sum + current robbery ( because we need to skip previous house if
                  robbing current house)
  
  TC: O(n)
  SC : O(1)
                  
  '''

class Solution:
    def rob(self, nums: List[int]) -> int:
    
        excl_sum=0
        incl_sum = nums[0]
        
        for currentHouse in range(1,len(nums)):
            prev_excl_sum = excl_sum
            prev_incl_sum = incl_sum
            incl_sum = prev_excl_sum + nums[currentHouse]
            excl_sum = max(prev_excl_sum,prev_incl_sum)
        
        return max(incl_sum, excl_sum)
