# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # the tree can be converted to graph by append connecting nodes for a node as parent,left, and right
        # then from given source we will do bfs and get all nodes of distance k
        def convert_into_graph(node, parent, g):
            # To convert into graph we need to know who is the parent
            if not node:
                return

            if parent:
                g[node].append(parent)

            if node.right:
                g[node].append(node.right)
                convert_into_graph(node.right, node, g)

            if node.left:
                g[node].append(node.left)
                convert_into_graph(node.left, node, g)
        
        g = defaultdict(list)
        vis, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        convert_into_graph(root, None, g)

        q.append((target, 0))

        while q:
            n, d = q.popleft()
            vis.add(n)

            if d == k:
                res.append(n.val)

            # adjacency list traversal
            for nei in g[n]:
                if nei not in vis:
                    q.append((nei, d + 1)) 

        return res
