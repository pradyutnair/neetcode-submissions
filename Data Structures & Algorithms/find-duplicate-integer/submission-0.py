class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = []
        dup = []

        for i in nums:
            if i not in unique:
                unique.append(i)
            elif i not in dup:
                dup.append(i)

        return dup[0]