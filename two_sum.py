class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked_nums = []
        indexes = []
        for i in range(len(nums)):
            for j in range(len(checked_nums)):
                if (nums[i] + checked_nums[j] == target) and (i != j) :
                    indexes.append(i)
                    indexes.append(j)
                    return indexes
                    break
            checked_nums.append(nums[i])