class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if (x == 0 or nums[x] > nums[x - 1]) and (x == len(nums) - 1 or nums[x] > nums[x + 1]):
                return x