class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1

            while q:
                row , column = q.popleft()
                for u,v in directions:
                    nr,nc = row + u , column + v
                    if (nr < 0 or nc <0 or nr >= m or nc >=n or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0


                    res +=1
            return res
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area,bfs(i,j))
        return area

                    

