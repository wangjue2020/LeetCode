class Solution:
    def maxProfit(self, prices) -> int:
        cur = 0
        ans = 0
        s = True
        for i in range(len(prices)):
            if s:
                cur = -prices[i]
                s = False
            elif cur < 0:
                if cur + prices[i] < 0 :
                    cur = -prices[i]
                else:
                    ans = max(ans, cur+prices[i])
            else:
                ans = max(ans, cur+prices[i])
        return ans