# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def find(root) -> int:
            nonlocal res
            if root is None:
                return 0
            leftSum = max(0,find(root.left))
            rightSum = max(0,find(root.right))
            res = max(res, root.val + leftSum+rightSum)
            return root.val + max(leftSum, rightSum)
        find(root)
        return res
    
