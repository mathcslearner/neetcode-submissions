from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # idea: do BFS starting from treasure chests
        INF = 2147483647
        WATER, TREASURE = -1, 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            visited = set([(r, c)])
            iteration = 1

            while q:
                curr_len = len(q)
                for i in range(curr_len):
                    row, col = q.popleft()
                    for direction in directions:
                        new_r = row + direction[0]
                        new_c = col + direction[1]
                        if (0 <= new_r < rows) and (0 <= new_c < cols) and grid[new_r][new_c] > 0:
                            if (new_r, new_c) not in visited:
                                q.append((new_r, new_c))
                                grid[new_r][new_c] = min(grid[new_r][new_c], iteration)
                                visited.add((new_r, new_c))
                            
                iteration += 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    bfs(r, c)
