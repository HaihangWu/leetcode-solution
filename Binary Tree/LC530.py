# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def Traverse(self, root, res):
        if root is None:
            return
        self.Traverse(root.left, res)
        res.append(root.val)
        self.Traverse(root.right, res)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.Traverse(root, res)
        return res

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=self.inorderTraversal(root)
        size=len(res)
        min_dif=res[1]-res[0]
        for i in range(size-1):
            min_dif=min(min_dif,res[i+1]-res[i])
        return min_dif
