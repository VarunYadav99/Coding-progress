"""         #Bruteforce#
class Solution:  # Time limit exceeds 
    def containsDuplicate(self, nums: List[int]) -> bool: 
        for i in range(len(nums)):  
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False """
class Solution:  # Most efficient in SPACE among the solutions
    def containsDuplicate(self, nums: List[int]) -> bool:   # Time: O(nlogn) and Space: O(1)
        nums.sort()
        l = 0
        r = l + 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l = l + 1
            r = l + 1
            
        return False      