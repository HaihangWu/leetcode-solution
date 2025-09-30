"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def order(self, root, depth, res):
        if root is None:
            return

        if len(res) == depth:
            res.append([])

        res[depth].append(root.val)

        for child in root.children:
            self.order(child, depth + 1, res)

    def levelOrder(self, root):
        """
        :type root: 'Node'
        :rtype: List[List[int]]
        """
        res = []
        self.order(root, 0, res)
        return res