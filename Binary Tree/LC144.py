class Solution(object):
    def Traverse(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.Traverse(root.left, res)
        self.Traverse(root.right, res)
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.Traverse(root, res)
        return res