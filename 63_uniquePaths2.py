class Solution:
    def uniquePathsWithObstacles(self, maze: List[List[int]]) -> int:

        def f(i,j,maze,dp):
            if maze[0][0] == 1:
                return 0
            if maze[i][j] == 1:
                return 0
            if i==0 and j==0 :
                return 1
            if i<0 or j<0 or maze[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]    
            up=f(i-1,j,maze,dp)
            left=f(i,j-1,maze,dp)
            dp[i][j]=left+up
            
            return dp[i][j]

        m=len(maze)
        n=len(maze[0])
        dp = [[-1 for j in range(n)] for i in range(m)]  
        return f(m-1,n-1,maze,dp)

        
