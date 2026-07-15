class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree property
        if len(edges) > n - 1:
            return False

        # Build an adjacency list
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
            
        return dfs(0, -1) and len(visited) == n