class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) <= 1:
            return [0]
        # brute force
        # res = []
        # for i, num in enumerate(temperatures):
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] < num:
        #             count += 1
        #     if count == len(temperatures) - i-1:
        #         count = 0
        #     res.append(count)
        # return res
        
        res = [0] * len(temperatures)
        stack = [] # (temp, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                T, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))
        return res



