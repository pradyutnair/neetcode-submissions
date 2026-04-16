class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        # brute force 
        result = []
        for i, a in enumerate(nums):
            pdt = 1
            for j, b in enumerate(nums):
                if i != j:
                    pdt *= b
            result.append(pdt)
        return result
        """
        map = {}
        l_pdt = 1
        for index, num in enumerate(nums):
            l_pdt *= num
            map[index] = l_pdt

        r_pdt = 1
        result = []
        
        for i in range(len(nums)-1, -1 ,-1):
            if i == len(nums) - 1:
                result.append(map[i-1])
            elif i > 0:
                result.append(r_pdt * map[i-1])
            else:
                result.append(r_pdt)
            r_pdt *= nums[i] 
        
        return result[::-1]
        


            
        


