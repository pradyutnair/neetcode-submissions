# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # DFS - Recursive
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp
        
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # BFS
        q = [root]
        while q:
            node, q = q[0], q[1:]
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root




            
