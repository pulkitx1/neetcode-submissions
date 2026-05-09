class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = float('inf')

        for i in range(n):
            for j in range(i + 1, n):

                # only take when future value is greater
                if prices[j] > prices[i]:
                    diff = prices[i] - prices[j]

                    # store smallest positive difference
                    if diff < ans:
                        ans = diff

        # if no profit possible
        if ans == float('inf'):
            return 0

        return -ans