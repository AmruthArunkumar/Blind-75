class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if grid[r][c] == "0": return
            if (r, c) not in visited:
                visited.add((r, c))
                bfs(r-1, c)
                bfs(r, c-1)
                bfs(r+1, c)
                bfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands