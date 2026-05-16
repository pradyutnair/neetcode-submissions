class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diam = 0

        def dfs(root):
            if not root:
                return 0

            # Get left and right heights
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            # for each node
            # Keep track of max_diam: max of curr diam vs sum of left+right diams
            self.max_diam = max(self.max_diam, left_h+right_h)
            
            # Diameter =  Current node + max of its left and right heights
            return 1 + max(left_h, right_h)
        
        # Run dfs 
        dfs(root)
        return self.max_diam

