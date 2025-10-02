# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            if root.right is not None:
                smallest_node = root.right
                while smallest_node.left is not None:
                    smallest_node = smallest_node.left
                smallest_node.left = root.left
                root = root.right
            else:
                root = root.left
        else:
            if root.left is None and root.right is None:
                return root
            if key > root.val:
                if root.right is None:
                    root.right = TreeNode(key)
                else:
                    root.right = self.deleteNode(root.right, key)
            else:
                if root.left is None:
                    root.left = TreeNode(key)
                else:
                    root.left = self.deleteNode(root.left, key)
        return root

