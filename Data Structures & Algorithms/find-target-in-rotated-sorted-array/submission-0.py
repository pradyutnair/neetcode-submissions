class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        index = 0

        while L <= R:
            M = (L+R)//2
            if target == nums[M]:
                return M

            # left sorted portion
            if nums[L] <= nums[M]:
                if target > nums[M] or target < nums[L]:
                    L = M + 1
                else:
                    R = M - 1
            # right sorted portion
            else:
                if target < nums[M] or target > nums[R]:
                    R = M - 1
                else:
                    L = M + 1
        return -1