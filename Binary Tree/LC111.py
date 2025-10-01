# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def order(self, root, depth, res):
        if root is None:
            return

        if (len(res) == depth):
            res.append([])

        if root.left is None and root.right is None:
            res[depth].append(1)  # leaf node
        else:
            res[depth].append(0)
        self.order(root.left, depth + 1, res)
        self.order(root.right, depth + 1, res)

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        depth = 0
        self.order(root, depth, res)
        depth = 0
        print(res)
        for ele in res:
            depth += 1
            if sum(ele) > 0:
                break
        return depth
