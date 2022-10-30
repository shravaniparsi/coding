# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        # since it's sorted array middle element must be root
        mid = len(nums)//2
        middle = nums[mid]
        print(mid)
        bt = TreeNode(middle)
        bt.left = self.sortedArrayToBST(nums[:mid])
        bt.right = self.sortedArrayToBST(nums[mid+1:])
        return bt
        
