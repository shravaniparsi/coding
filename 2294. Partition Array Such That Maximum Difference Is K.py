class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # we sort the array
        # we take initially nums[0] the max value
        # and from index 1 to length we check if any position nums[0]/initial - nums[i] exceeding k
        # if yes we partion there and start checking from that position
        # each time we reset we increment the result
        nums.sort(reverse = True)
        
        initial = nums[0]
        count = 0
        for i in range(1, len(nums)):
            if initial - nums[i] > k:
                initial = nums[i]
                count += 1
        count += 1
        return count
        
