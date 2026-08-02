class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {i: False for i in range(n)}
        adj_list = {i : [] for i in range(n)}
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        
        def bfs(adj_list,source):
            from collections import deque

            q = deque()
            visited[source] = True
            q.append(source)
            
            while q:
                node = q.popleft()
                for k in adj_list[node]:
                    if not visited[k]:
                        visited[k]  =True
                        q.append(k)
        n_comp = 0
        for i in range(n):
            if visited[i] == False:
                n_comp += 1
                bfs(adj_list, i)
        return n_comp
            