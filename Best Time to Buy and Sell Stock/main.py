class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        max_global = 0
        chosen_price = prices[0]
        for price in prices:
            max_current = max(price - chosen_price, 0)
            max_global = max(max_global, max_current)
            chosen_price = min(chosen_price, price)

        return max_global


sol = Solution()
print(sol.maxProfit([4,3,2,5]))
