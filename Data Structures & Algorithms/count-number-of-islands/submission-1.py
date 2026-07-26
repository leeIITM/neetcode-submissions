class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        def bfs(grid, node):
            sx, sy = node
            q = deque()
            q.append([sx,sy])
            visited[sx][sy] = True
            while q:
                a,b = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                neighbours = []
                for u,v in directions:
                    if a + u  < 0 or a + u >= m or b + v < 0 or b + v >= n:
                        pass
                    else:
                        if grid[a+u][b+v] == "1":
                            neighbours.append([a+u, b+v])
                for c ,d in neighbours:
                    if not visited[c][d]:
                        visited[c][d] = True
                        q.append([c,d])
        comp = 0
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "1" and not visited[i][j]:
                    comp +=1
                    bfs(grid,[i,j])
        return comp


