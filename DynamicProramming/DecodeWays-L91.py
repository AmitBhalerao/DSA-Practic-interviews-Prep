'''
DP problem with memoization.

At every step you have two option to choose one char or two char from the input string.
If it's valid char then proceed explore rest of the string with same logic.

return 1 if you reach end of the string
return 1 if you reach 2nd last char, this is to avoid twochar check from this point.
return 0 if any particular char is not valid

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        
        encodelist = [str(i) for i in range(1,27)]
        curr_index= 0
        memo={}
        return self.DP_decodeWays(s,curr_index,encodelist,memo)
        
    def DP_decodeWays(self,s:str,curr_index:int,encodelist:List[str],memo:dict)->int:
        
        
        if curr_index >= len(s):
            return 1
        
        if s[curr_index] not in encodelist:
            return 0
        
        # this is to avoid twochar call (line 31) because it will still consider last char
        if curr_index >= len(s)-1:
            return 1
        
        
        #memo to avoid TLE
        if curr_index in memo:
            return memo[curr_index]
        
        ans=0
        if s[curr_index:curr_index+1:] in encodelist:
            ans += self.DP_decodeWays(s,curr_index+1,encodelist,memo)
            
        if s[curr_index:curr_index+2:] in encodelist:
            ans += self.DP_decodeWays(s,curr_index+2,encodelist,memo)
        
        memo[curr_index] = ans
        
        return memo[curr_index]
