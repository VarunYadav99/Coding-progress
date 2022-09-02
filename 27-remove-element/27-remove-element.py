"""class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        
        for index in range(len(nums)):
            if nums[index] != val:
                nums[left] = nums[index]
                left += 1

        return left
    """
class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		length = len(nums)
		index = 0
		while index < length:
			if nums[index] == val:
				nums[index] = nums[length - 1]
				length -= 1
			else: index += 1
		return length
