class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0


        i, j = 0, len(nums)
        while i < j:
            # 0 + len(list) == total length of list. // 2 = midpoint
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        return -1


