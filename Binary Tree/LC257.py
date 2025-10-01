# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def path(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [str(node.val)]

            paths=[]
            for child in (node.left,node.right):
                for subpath in path(child):
                    paths.append(str(node.val)+'->'+subpath)

            return paths


        return path(root)