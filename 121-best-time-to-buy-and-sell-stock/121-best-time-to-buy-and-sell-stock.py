"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0
        while r < (len(prices)):
            if prices[l]<prices[r]:
                profit = r - l
                maxp= max(maxp,profit)
            else:
                l = r
                r += 1
        return maxp
                """
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit