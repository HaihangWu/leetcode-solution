# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if len(postorder) == 0:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        d_index = inorder.index(root_val)

        left_tree_in = inorder[0:d_index]
        right_tree_in = inorder[d_index + 1:]

        left_tree_post = postorder[0:d_index]
        right_tree_post = postorder[d_index:-1]
        root.left = self.buildTree(left_tree_in, left_tree_post)
        root.right = self.buildTree(right_tree_in, right_tree_post)

        return root

