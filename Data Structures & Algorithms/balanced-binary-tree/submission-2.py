# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def dfs(root):
            nonlocal ans
            if ans == False:
                return 0
            if root is None:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)
            if abs(lh-rh) > 1:
                ans =  False
            return 1 + max(lh, rh)
        dfs(root)
        return ans