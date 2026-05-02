class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = []
        nums_set = set(nums)
        all_seqs = []
        if not nums:
            return 0
        # Only elements i that don't have i-1 in map, are starts of sequences
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                # Thats a sequence start
                start = nums[i]
                seq = [start]
                # Get the length of the sequence using the start
                j = start + 1
                while True:
                    if j in nums_set:
                        seq.append(j)
                    else:
                        break
                    j += 1
                all_seqs.append(len(seq))
        return max(all_seqs)




                
