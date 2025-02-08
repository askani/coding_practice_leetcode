

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Using Hashmap
        valueMap = {} # value : index pairs

        for i, n in enumerate(nums):
            difference = target - n
            if difference in valueMap:
                return [valueMap[difference], i]
            valueMap[n] = i
        return

def main():
    func_ = Solution()
    a = list(map(int, input("Enter list of input integers").split()))
    b = int(input("Enter the target sum"))
    print(func_.twoSum(a, b))

if __name__ == "__main__":
    main()
