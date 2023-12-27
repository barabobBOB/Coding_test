# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        max_level = -1

        def dfs(node, level):
            nonlocal max_level
            if level > max_level:
                result.append(node.val)
                max_level = level

            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 0)
        return result
