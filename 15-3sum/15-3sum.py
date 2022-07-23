"""class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue 
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # We sort nums first to more easily find duplicate numbers
        triplets = [] # We will store all the valid triplets in here
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue # Skip duplicates
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1;
                    
                    # Skip all duplicates on left side
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    
                    # Skip all duplicates on right side
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif curSum < 0:
                    left += 1 # Our sum is too small, so we try to increase the sum
                else:
                    right -= 1 # Our sum is too big, so we try to decrease the sum
        return triplets
