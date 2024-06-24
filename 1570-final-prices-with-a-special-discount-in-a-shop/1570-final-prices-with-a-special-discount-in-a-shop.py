class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        list = []
        for i in range(len(prices)):
            count = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    count = prices[j]
                    break
            list.append(prices[i] - count)
        return list