'''
Points to remember:
1. DP+ recursive written in such way that we base case are diceIndex==0,target==0 conditions are checked. 
2. Recursive calls starts from dice_index=n then reducing the count for each recursive call.
3. all face values are tried for particular dice_index and target value reduced by current_face value for next recursive call and next dice_index.

'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo={}
        return self.totalway(n,k,target,memo)
    
    def totalway(self,start_dice,k,target,memo):
        if target == 0 and start_dice==0:
            return 1
        if target < 0 or start_dice <= 0:
            return 0
        ways = 0
        MOD=1000000007
        key = str(start_dice)+'-'+str(target)
        
        #print("lin17 memo:{}".format(memo))
        if key in memo:
            return memo[key]
        
        
        #for dice in range(start_dice,n+1):
            
        for face in range(1,k+1):
            if target<face: #optimization
                break;
            temp = self.totalway(start_dice-1,k,target-face,memo) % MOD
            ways = ways%MOD
            ways = (ways+temp)%MOD

        memo[key]=ways
        return ways
