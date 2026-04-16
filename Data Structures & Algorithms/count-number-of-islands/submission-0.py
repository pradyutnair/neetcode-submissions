class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Grid shape
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(r,c, visit):
            # If its out of bounds, or already visited or a 0, then break out of search
            if min(r,c) < 0 or (r,c) in visit or r == ROWS or c == COLUMNS or grid[r][c] == '0':
                return 
            # Mark the current coord as visited
            visit.add((r,c))
            # Traverse right, left, up, down
            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)

        islands = 0
        visit = set()
        # For all cells, only run when a 1 is present and not already visited
        for r in range(ROWS):
            for c in range(COLUMNS):
                # When we find an unvisited 1, that's an island
                if grid[r][c] == '1' and (r,c) not in visit:
                    islands+=1
                    # Find and mark everything around that 1
                    dfs(r,c,visit)
        return islands