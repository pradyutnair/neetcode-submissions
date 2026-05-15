# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = [root]
        depth = 0
        while dq:
            n_nodes = len(dq)
            popped, dq = dq[:n_nodes], dq[n_nodes:]
            for node in popped:
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth+=1
        return depth

            