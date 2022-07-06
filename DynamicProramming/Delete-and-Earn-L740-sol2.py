'''
This solution is DP solution bottom-up approach.
(Earlier submission contains top-down approch)

TC: O(N log(N)) where N= len(nums) 
SC: O(N)  O(N) for frequency list

Point to note:

There can be un-necessory calls for num because of num-1 and num-2 call even though those numbers are not present in nums. This can be avoided if we check if next traverse nums array and unless next number is num+1, we can directly add frequency(num+1) to our so far earnings. If it's num+1 then we need to use max(DP(num-1),DP(num-2)+freq[num])


Optimization:

1. Now we need only previous 2 values, one_back and two_back so why to use and mantain whole list of memo_list

2. How to avoid un-necessory DP(num) calculations if num is not present in input array?
    By sorting frequency on the basis of keys

'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        max_number = 0
        
        for num in nums:
            frequency[num] += num
            max_number = max(max_number,num)
        
        
        
        return self.DP_deleteAndEarn(max_number,frequency)
    
    def DP_deleteAndEarn(self,max_number,frequency):
        
        #creating memo list of size max_number+1
        
        sorted_keys = sorted(frequency.keys())
        
        two_back = 0
        one_back = frequency[sorted_keys[0]] #minimum key freq value
        
        for i in range(1,len(sorted_keys)):
            current_element = sorted_keys[i]
            
            # if current_element is not immediate next number then we can directly add it's frequency points to one_back and continue to next calculation
            if current_element > (sorted_keys[i-1] + 1):
                two_back,one_back = one_back, (one_back + frequency[current_element])
            else:
                #current one_back becomes two_back for next
                #next one_back will be max(current one_back, two_back + frequency[i])
                two_back,one_back = one_back, max(one_back,two_back+frequency[current_element])
        
        
        return one_back
        
        
        
        
        
