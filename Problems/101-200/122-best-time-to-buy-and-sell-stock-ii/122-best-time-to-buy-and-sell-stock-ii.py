class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices[0] = -prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i]+prices[i-1] > 0:
                ans += prices[i]+prices[i-1]
                prices[i] = -prices[i]
            else:
                prices[i] = -prices[i]
        return ans