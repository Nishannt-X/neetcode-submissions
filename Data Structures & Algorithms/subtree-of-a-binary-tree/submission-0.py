# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def same(n,s):
            if not n and not s:
                return True
            if not n or not s:
                return False
            if n.val!=s.val:
                return False
            return (same(n.left,s.left) and same(n.right,s.right))

        def dfs(node):

            if not node:
                return False

            if node.val==subRoot.val:
                if same(node,subRoot):
                    return True
            
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

        