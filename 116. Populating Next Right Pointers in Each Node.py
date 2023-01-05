"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def connectleft(root):
            if root.left:
                root.left.next = root.right
                connectleft(root.left)
            if root.right:
                root.right.next = root.next.left if root.next else None
                connectleft(root.right)
                
        if root:
            root.next=None
            connectleft(root)
            
        return root
