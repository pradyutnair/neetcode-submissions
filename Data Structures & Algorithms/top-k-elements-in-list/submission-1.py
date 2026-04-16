from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        # Counter: number: freq
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        # Bucket sort
        n = len(nums)
        # [[], [].. []]
        buckets = [[] for _ in range(n+1)]

        # Reverse counter: freq: [all numbers that have that freq]
        for num, freq in res.items():
            buckets[freq].append(num)
        
        res = []
        # Go from n to 0 (all freqs < n)
        for i in range(n, 0, -1):
            # For all numbers that have freq = i
            for num in buckets[i]:
                res.append(num)
                # check if we hit the k limit
                if len(res) == k:
                    return res
        return res