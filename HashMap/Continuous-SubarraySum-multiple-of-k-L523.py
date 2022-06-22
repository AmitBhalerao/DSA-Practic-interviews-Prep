'''
Prefixsum approach is used along with hashmap
Similar approach can be used to find count of subarrays with 0 sum or longest subarray with 0 sum.


Difference here is that prefixsum%k is checked if present in the hashmap. 

So if there are two index where prefixSum % k is same then that means that subarray sum is multiple for k. So if differnce between these indexes (subaray length) are more than 2 (in this example) then we can return true
TC: O(n)
SC: O(n)
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefixSum = 0
        hashmap={0:-1}
        
        for index in range(len(nums)):
            prefixSum += nums[index]
            
            if prefixSum%k in hashmap:
                if index - hashmap[prefixSum%k] >=2:
                    return True
            
            else:
                hashmap[prefixSum%k] = index
        
        return False
