"""LINEAR SEARCH"""
""" class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if (x == 0 or nums[x] > nums[x - 1]) and (x == len(nums) - 1 or nums[x] > nums[x + 1]):
                return x"""
class Solution:
    def findPeakElement(self, nums: List[int])-> int:
        l,r=0,len(nums)-1
        while l <= r: 
            mid  =(l +r)//2
            if (mid > 0 and nums[mid -1] > nums[mid]):
                    r = mid -1 
            elif (mid<len(nums)-1 and nums[mid + 1] > nums[mid]):
                    l = mid + 1
            else:
                  return mid
            
                