'''
TC: O(N!)
SC: O(N^2)
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #try to place first queen in all possible places in first row in order to explore all combinations
        ans=[]
        grid = [['.' for _ in range(n)] for _ in range(n)]
        
        self.backtracking_nQueens(grid,0,n,ans)
        
        return ans
        
        #use backtracking algo
    
    def backtracking_nQueens(self,grid,current_row,n,ans):
        
        if current_row == n:
            temp=[]
            for i in range(n):
                temp.append(''.join(grid[i]))
            ans.append(temp)
            return
        
        for col in range(n):
            if self.isValid(grid,current_row,col,n):
                grid[current_row][col] = 'Q'
                self.backtracking_nQueens(grid,current_row+1,n,ans)
                grid[current_row][col] = '.'
        
        return
        
    def isValid(self,grid,row,col,n):
        #row validity:
        for i in range(n):
            if grid[row][i] == 'Q':
                return False
        
        #col validity
        for j in range(n):
            if grid[j][col] == 'Q' :
                return False
            
        
        #diagonal validity
        x=row-1
        y=col-1
        
        while(x>=0 and y>=0):
            if grid[x][y] == 'Q':
                return False
            x = x-1
            y = y-1
        
        
        x = row-1
        y = col+1
        
        while(x>=0 and y<n):
            if grid[x][y]=='Q':
                return False
            x = x-1
            y = y+1
        
        return True
            
        
        
        #if you able to place all queens then add it so solution and return
        
    
    
        
        
