'''
Sliding window problem
See the code notes
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        window_start,window_end = 0,0
        
        char_freq={}
        max_len = 0
        
        #to track max repeat so far 
        max_repeat=0
        
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in char_freq:
                char_freq[char]=0
            
            char_freq[char] += 1
            max_repeat = max(max_repeat,char_freq[char])
            
            # now max allowed chages are k, so if current window length - max_repeat will give you
            # total changes needs to be done to get repeating characters
            # if this current window length - max_repeat is more than k then increment window_start
            # and reduce the freq of s[window_start]
            
            if (window_end - window_start +1 - max_repeat) > k:
                char = s[window_start]
                char_freq[char] -= 1
                window_start += 1
            
            max_len = max(max_len,window_end-window_start+1)
        
        return max_len
        
        
