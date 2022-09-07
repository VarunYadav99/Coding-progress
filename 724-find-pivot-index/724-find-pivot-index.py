class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Total  = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = Total - nums[i] - leftSum          
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1        