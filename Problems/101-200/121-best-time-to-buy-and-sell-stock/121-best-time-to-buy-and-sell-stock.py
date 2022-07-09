class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur = -prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, cur + prices[i])
            cur = max(cur, -prices[i])
        return ans