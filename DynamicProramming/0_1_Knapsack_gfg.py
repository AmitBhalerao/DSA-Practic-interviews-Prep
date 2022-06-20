#User function Template for python3
'''
DP problem

key trick: consider and notconsider pattern and solve it using memoisation to avoid TLE.

You can create binary tree for the states code will go through if you solve it manually.

'''

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        memo = {}
        return self.DP_knapsack(W,wt,val,0,memo)
        
    def DP_knapsack(self,capacity,wt,val,currentitem,memo):
        
        if currentitem==len(wt):
            return 0
        
        key = str(capacity)+'-'+str(currentitem)
        
        if key in memo:
            return memo[key]
        
        consider,notconside = 0,0
        
        if capacity >= wt[currentitem]:
            consider = val[currentitem]+self.DP_knapsack(capacity-wt[currentitem],wt,val,currentitem+1,memo)
        
        notconsider = self.DP_knapsack(capacity,wt,val,currentitem+1,memo)
        
        
        memo[key]= max(consider,notconsider)
        
        return memo[key]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
