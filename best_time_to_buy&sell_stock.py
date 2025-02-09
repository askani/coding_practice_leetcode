class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            elif profit < (price - minPrice):
                profit = price - minPrice
        return profit

def main():
    func_ = Solution()
    a = list(map(int, input("Enter list of stock prices").split()))
    print(func_.maxProfit(a))

if __name__ == "__main__":
    main()