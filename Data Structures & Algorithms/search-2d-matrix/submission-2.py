class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Treat the whole matrix as a flat sorted array of size ROWS*COLS
        l, r = 0, ROWS * COLS - 1 

        while l <= r:
            mid = (l + r) // 2

            # Convert flat index → 2D coords
            # e.g. index 9 in a 4-col matrix: row = 9//4 = 2, col = 9%4 = 1
            row = mid // COLS  # full rows that fit before index mid
            col = mid % COLS   # steps into the current row (the leftover)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1    # mid is too big → discard right half
            else:
                l = mid + 1    # mid is too small → discard left half

        return False