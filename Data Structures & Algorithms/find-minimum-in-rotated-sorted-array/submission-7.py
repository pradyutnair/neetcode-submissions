class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        Min = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                Min = min(Min, nums[L])
                break

            M = (L+R) // 2
            Min = min(Min, nums[M])
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1
        return Min
            
