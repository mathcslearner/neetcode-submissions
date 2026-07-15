class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        currnode = 0

        # build adjacency list
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)

        while len(visited) != n:
            while currnode in visited:
                currnode += 1
            dfs(currnode, -1)
            count += 1

        return count