class Solution:
    def trap(self, height: List[int]) -> int:
        maxl= []
        maxr = []
        res = 0
        for i in range(len(height)):
            maxl.append(max(height[:i]) if height[:i] else 0)

        for j in range(len(height)):
            maxr.append(max(height[j+1:]) if height[j+1:] else 0)

        for k in range(len(height)):
            # Water = min(maxl, maxr) - height[k]. If negative, then 0
            water = max(min(maxl[k], maxr[k]) - height[k], 0)
            res += water

        return res