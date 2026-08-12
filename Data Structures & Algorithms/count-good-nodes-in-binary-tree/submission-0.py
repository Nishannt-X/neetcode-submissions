# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        q=deque([(root,root.val)])
        ans=0

        while q:
            node,maxi=q.popleft()

            if node.val>=maxi:
                ans+=1
            maxi=max(maxi,node.val)

            if node.left:
                q.append((node.left,maxi))
            if node.right:
                q.append((node.right,maxi))
            
        return ans
            

            
            

        

        