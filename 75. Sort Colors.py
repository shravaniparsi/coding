class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        
        i = 0 # index being checked
        count = 0 # number of elements already sorted
        while count < len(nums):
            if nums[i] == 0: # if 0 is found, place it in p0
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1 # increment p0 so that next time when 0 is found, it will be put into correct position
                i += 1 # move on to the next element in iteration
            elif nums[i] == 1: # if it is a 1, do nothing, just move on to next element
                i += 1
            else: # if it is a 2, swap the elements and decrement p2. Since we dont know what elements we got swapped with from p2, it still needs to be checked. So dont increment i. 
                nums[i], nums[p2] = nums[p2], nums[i]
                p2-=1
            count += 1 # every iteration of while loop puts one element at correct position
