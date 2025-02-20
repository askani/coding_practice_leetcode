class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxP = float("-inf")
        i , j = 0 , len(nums)-1
        pre , suff = 1 , 1

        while j >= 0 and i < len(nums):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1

            pre *= nums[i]
            suff *= nums[j]
            maxP = max(maxP , pre , suff)
            i += 1
            j -= 1

        return maxP

def main():
    func_ = Solution()
    a = list(map(int, input("Enter list of integers").split()))
    print(func_.maxProduct(a))

if __name__ == "__main__":
    main()