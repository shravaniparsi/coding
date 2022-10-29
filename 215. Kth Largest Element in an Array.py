class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortednums = sorted(nums)[::-1]
        return sortednums[k-1]
