from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in pair:
                return [pair[m], i]
            else:
                pair[n] = i
        return None
            

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    result = Solution2().twoSum(nums, target)
    print(result)