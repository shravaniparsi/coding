class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid,i,j):
            #edge cases
            if i< 0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            
            # we mark as # to keep track of visited islands
            grid[i][j] = "#"
            
            # we dodfs and mark all adjacent as #
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            
        # edge cases
        if not grid:
            return 0
        
        # initializing to 0 
        numberofislands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    #if it is 1 we will do dfs, each time we do dfs it is +1 of island
                    dfs(grid,i,j)
                    numberofislands += 1
        return numberofislands
        
# Time: O(NM) N number of rows, M number of cols
# Space: O(NM)
