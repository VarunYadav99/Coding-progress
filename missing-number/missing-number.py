class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums) + 1 
        for i in range (n):
            if i not in nums_set:
                return i