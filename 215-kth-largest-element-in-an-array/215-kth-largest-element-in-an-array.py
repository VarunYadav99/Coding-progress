"""class Solution:
    
        def findKthLargest3(self, nums, k):
             for i in xrange(len(nums), len(nums)-k, -1):
                tmp = 0
                for j in xrange(i):
                    if nums[j] > nums[tmp]:
                        tmp = j
                      nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
                  return nums[len(nums)-k]"""
class Solution:
    
    
    def partition(self, nums, left, right):
        
        pivot = nums[left]
        l, r = left+1, right
        
        while l <= r:
            
            if nums[l] < pivot and nums[r] > pivot:
                
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
            
            if nums[l] >= pivot:
                l += 1
            
            if nums[r] <= pivot:
                r -= 1
        
        
        nums[left], nums[r] = nums[r], nums[left]
        return r

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        left, right = 0, size-1
        
        while True:
            
            cur_index = self.partition( nums, left, right)
            
            if cur_index > k-1:
                right = cur_index -1
                
            elif cur_index < k - 1:
                left = cur_index + 1
            
            else:
                return nums[ cur_index ]