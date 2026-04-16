class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        # overall_profit = 0
        # for i in range(len(prices)):
        #     max_profit = 0
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        #     if max_profit > overall_profit:
        #         overall_profit = max_profit
        # return overall_profit

        # For each day, keep track of what was the minimum day seen so far
        # and calculate current profit to keep track of the max profit
        window_min = prices[0]
        max_profit = 0
        for i in prices[1:]:
            curr_profit = i - window_min
            if curr_profit > max_profit:
                max_profit = curr_profit
            if i < window_min:
                window_min = i
        return max_profit



        
