class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        areas = []

        def dfs(r,c,visit):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 0 
    
            visit.add((r,c))

            islands = 1
            islands += dfs(r+1,c,visit)
            islands += dfs(r-1,c,visit)
            islands += dfs(r,c+1,visit)
            islands += dfs(r,c-1,visit)
            return islands

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    islands = dfs(r,c,visit)
                    areas.append(islands)
        
        return max(areas) if areas else 0
                