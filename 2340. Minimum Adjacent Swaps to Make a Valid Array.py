class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        min_i = nums.index(min_)
        max_i = len(nums) - 1 - nums[::-1].index(max_) # since we reverse and try to find from begimg and we need index from end position
        return (len(nums) - 1 - max_i)+(min_i-1) if min_i > max_i else (len(nums) - 1 - max_i)+(min_i)
        
