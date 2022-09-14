class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        i = 0
        while(i < len(nums)):
            count = 0
            while(i < len(nums) and nums[i] == 1):
                count += 1
                i += 1
            if(max1 < count):
                max1 = count 
            i += 1
        return max1