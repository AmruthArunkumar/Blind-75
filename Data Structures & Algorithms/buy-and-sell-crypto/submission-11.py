class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxAfterMin = prices[0]
        maxProfit = 0
        for p in prices:
            prevMin = minSoFar
            minSoFar = min(minSoFar, p)
            if p > minSoFar:
                if p > maxAfterMin:
                    maxAfterMin = p
            elif prevMin != p:
                maxAfterMin = minSoFar
            maxProfit = max(maxProfit, maxAfterMin - minSoFar)
        return maxProfit