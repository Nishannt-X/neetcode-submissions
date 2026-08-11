class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float("inf")
        prof=0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            
            prof=max(prof,prices[i]-mini)
        return prof


        