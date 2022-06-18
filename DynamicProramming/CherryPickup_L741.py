'''
Trick:
1. instead of thinking about the backward path seperately why don't we find two best forward paths from 0,0 to N-1.N-1 such that maximum cherry can be picked.
2. In above case you just need to avoid counting cherry twice if path crosses same cell.


Now from 0,0 to N-1,N-1, steps required are constant, doesn't matter which path you take.

so lets track path1 and path2 via 2 pairs of(r,c)
path1: r1,c1 and path2: r2,c2

r1+c1 = r2+c2 at any point of time because both paths are moving togther or basically taking same number of step.

so r2=r1+c1-c2

using above equation and 3-D DP, problem can be solved.


'''



class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # size of grid
        N = len(grid)
        
        #starting two forwards paths from (0,0) position
        r1_start=c1_start=c2_start=0 
        
        #memo
        memo={}
        
        #dp call
        #if path doesn't exist then DP call return float('-inf')
        return max(0,self.DP_cherryPickup(grid,N,r1_start,c1_start,c2_start,memo))
    
    
    def DP_cherryPickup(self,grid,N,r1,c1,c2,memo):
        cherryPicked=0
        #r2 calculation
        r2=r1+c1-c2
        
        #key for memo:
        key = str(r1)+'-'+str(c1)+'-'+str(c2)
        
        #border check and thorn check
        if r1 == N or r2 == N or c1 == N or c2 == N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        #if reached destination
        elif r1 == c1 == N-1:
            return grid[r1][c1]
        elif key in memo:
            return memo[key]
        else:
            cherryPicked = grid[r1][c1]
            
            # add 2nd path cherry if it's not same position. if position is same then c1==c2 and r1==r2
            if c1!=c2:
                cherryPicked += grid[r2][c2]
            
            #dp call
            
            cherryPicked += max(self.DP_cherryPickup(grid,N,r1,c1+1,c2+1,memo),
                               self.DP_cherryPickup(grid,N,r1,c1+1,c2,memo),
                               self.DP_cherryPickup(grid,N,r1+1,c1,c2+1,memo),
                               self.DP_cherryPickup(grid,N,r1+1,c1,c2,memo))
            
        memo[key] = cherryPicked
        
        return memo[key]
            
            
            
        
        
        
