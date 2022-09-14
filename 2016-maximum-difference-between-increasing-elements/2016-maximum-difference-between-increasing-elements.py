class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = 0
        i,j = 0,1
        while j < len(nums):
            if i < j and nums[i] < nums[j]:
                m = max(m, nums[j]-nums[i])
                
            if nums[i] > nums[j]:
                i = j
                j+=1
            else:
                j+=1
        return m if m > 0 else -1
        """The First approch #brute-force method
using double for loop"""
        """maxv = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and nums[i] < nums[j]:
                    maxv = max(maxv, nums[j] - nums[i])
        return maxv if maxv > 0 else -1"""
"""Second approch using pointers

the problem statement defines it -> if nums[i] < nums[j] and i < j
so implementing it easy
m = 0
        i,j = 0,1
        while j < len(nums):
            if i < j and nums[i] < nums[j]:
                m = max(m, nums[j]-nums[i])
                
            if nums[i] > nums[j]:
                i = j
                j+=1
            else:
                j+=1
        return m if m > 0 else -1"""
        