# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        print(root)
        if targetSum is None or root is None:
            return []
        res=[]
        
        def dfs(root,currsum,currpath):
            if root is None:
                return
            # leaft node check if equal to target
            elif root and root.left is None and root.right is None and root.val+currsum == targetSum:
                currpath.append(root.val)
                res.append(currpath)
            # else continue
            else:
                dfs(root.left,currsum+root.val,currpath+[root.val])
                dfs(root.right,currsum+root.val,currpath+[root.val])
        
        dfs(root,0,[])
        return res
                
            
        
        
