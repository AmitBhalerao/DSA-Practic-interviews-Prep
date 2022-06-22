'''
Prefixsum approach is used along with hashmap

Similar approach can be used to find count of subarrays with 0 sum or longest subarray with 0 sum.

Difference here is that prefixsum-k is checked if present in the hashmap. 
So if there are two index where prefixSum difference is k then that means that subarray sum can be k.

TC: O(n)
SC: O(n)

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        hashmap={}
        prefixSum=0
        hashmap[0]=1
        
        for index in range(len(nums)):
            prefixSum += nums[index]
            if prefixSum-k in hashmap:
                ans += hashmap[prefixSum-k]
            
            if prefixSum in hashmap:
                hashmap[prefixSum] += 1
            else:
                hashmap[prefixSum] = 1
            
       # print(hashmap)
        
        return ans
                
            
        
