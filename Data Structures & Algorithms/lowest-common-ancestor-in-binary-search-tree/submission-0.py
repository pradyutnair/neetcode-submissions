class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ## Recursive
        # if not root:
        #     return None
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # return root

        ## Iterative
        cur = root
        while cur:
            # If p & q > current node, go right
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            # if p & q < current node, go left
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            # p,q are on either side: this is the LCA
            else:
                return cur