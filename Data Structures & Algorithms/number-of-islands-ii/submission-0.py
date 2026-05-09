class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # If you do this, it creates a ref to the same cols in every row
        # Modifying one value modifies them all which is wrong
        # cols = [0] * n   # [0, 0 .. ]
        # grid = [cols] * m # [[0, 0..], [0,0..], ..]

        
        
        def dfs(r, c , visit):
            if min(r, c) < 0 or r >= m or c >= n or (r,c) in visit or grid[r][c] == 0:
                return
            
            visit.add((r, c))
            dfs(r-1, c, visit)
            dfs(r+1, c, visit)
            dfs(r, c-1, visit)
            dfs(r, c+1, visit)
        
        # Grid
        grid = [[0]*n for _ in range(m)]
        r,c = 0, 0
        res = []
        for pos in positions:
            islands = 0
            visit = set()
            grid[pos[0]][pos[1]] = 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visit:
                        islands += 1
                        dfs(i, j, visit)
            res.append(islands)
        return res
