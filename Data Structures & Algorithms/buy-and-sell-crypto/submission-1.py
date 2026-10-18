class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i=0
        j=i+1
        while i<=j and j<len(prices):
            d=prices[j]-prices[i]
            if d<0:
                i+=1
            else:
                profit=max(profit,d)
                j+=1
        return profit



        
            


            