'''
DP solution top-down approach

TC: O(N+k) where N= len(nums) and k is max-number
SC: O(N+k)  O(N) for frequency list and O(k) for recursive stack and memo

Point to note:

There can be un-necessory calls for num because of num-1 and num-2 call even though those numbers are not present in nums. This can be avoided if we check if next traverse nums array and unless next number is num+1, we can directly add frequency(num+1) to our so far earnings. If it's num+1 then we need to use max(DP(num-1),DP(num-2)+freq[num])

'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        max_number = 0
        
        for num in nums:
            frequency[num] += num
            max_number = max(max_number,num)
        
        memo = {}
        
        return self.DP_deleteAndEarn(max_number,frequency,memo)
    
    def DP_deleteAndEarn(self,num,frequency,memo):
        
        #print("num: {} memo:{}".format(num,memo))
        if num == 0:
            return 0
        
        if num == 1:
            return frequency[num]
        
        if num in memo:
            return memo[num]
        
        consider = frequency[num] + self.DP_deleteAndEarn(num-2,frequency,memo)
        notconsider = self.DP_deleteAndEarn(num-1,frequency,memo)
        
        
        memo[num] = max(consider,notconsider)
        #print("second print num: {} memo:{}".format(num,memo))
        return memo[num]
        
        
        
        
        
