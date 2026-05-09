class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ans = 0

        for i in range(1, len(prices)):

            # profit if sold today
            profit = prices[i] - mini

            # store maximum profit
            ans = max(ans, profit)

            # update minimum buying price
            mini = min(mini, prices[i])

        return ans