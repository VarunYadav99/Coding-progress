class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp = nums.copy() 
        
        shift = k % len(nums)
        
        for i in range(len(tmp)):
            nums[i] = tmp[i-shift]
            
            
            
"""            start, we create a copy of nums to preserve the original element order because we will directly shift the elements in nums.

Next, we create our shift value by taking k % len(nums). This is because a shift value that is larger than the length of the array is a repetition. E.g. a shift of 7 elements on an array of size 4 is the same as shifting 3 elements on an array of size 4.

Finally, we do one pass through our tmp array and shift the elements of nums by setting the current nums value to the value of (index - shift) from the tmp array. The reason why this works is simple - for the elements from index 0 up to but not including shift, we are retrieving the values from the end of the list because of negative indexing. Then for the elements from shift to the end, we are moving the elements from the tmp array forward k times.

Example Explanation:
To give an example, within nums=[1,2,3,4,5,6,7] and k=3, a shift of 3 results in nums=[5,6,7,1,2,3,4]. When we iterate through our tmp, the first index we start on is 0 with a value of 5 in our result. If we take (index - shift), we get (0 - 3) resulting in -3. Python can index values starting from the rear of the list using negative indexing with the last element starting at an index of -1. If we look at the position of 5, it is at the -3rd position.

When we reach the shift index, we are now simply shifting the elements forward in indexes rather than fetching the negative index. Starting from the element at the shift index which is 1 in our example case, we see that 1 is the element at the 3rd index in our result list. When we take (index - shift) which is (3 - 3), we get 0, which is the position of 1 within tmp.

Complexity Explanation:
The O(n) time complexity comes from the python copy function running in linear time, as well as the for loop iterating through tmp.

The O(n) space complexity comes from nums.copy. Pythons copy function performs a shallow copy, meaning that our new array is actually a collection of elements that reference the elements in the original array. This operation still takes linear space because the references space scales with the input array size, however the actual space taken is still less than if we were to create a new array with the elements of nums."""