class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        # Set # of rows and cols
        ROWS, COLUMNS = len(image), len(image[0])
        # Original color
        oc = image[sr][sc]

        def dfs(sr, sc, visit):
            # Boundary conditions
            if min(sc, sr) < 0 or sr == ROWS or sc == COLUMNS or (sr, sc) in visit:
                return
            else:
                # Check if it does not have the same colour
                if image[sr][sc] != oc:
                    return
                else:
                    # Change it if it does
                    image[sr][sc] = color
            # Mark as visited
            visit.add((sr, sc))
            # Visit down, up, left, right
            dfs(sr - 1, sc, visit)
            dfs(sr + 1, sc, visit)
            dfs(sr, sc - 1, visit)
            dfs(sr, sc + 1, visit)
        
        dfs(sr, sc, visit)

        return image
