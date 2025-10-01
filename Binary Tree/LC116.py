"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def order(self, root, depth, res):
        if root is None:
            return

        if (len(res) == depth):
            res.append([])

        if res[depth]:
            res[depth][-1].next = root

        res[depth].append(root)

        self.order(root.left, depth + 1, res)
        self.order(root.right, depth + 1, res)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        res = []
        depth = 0
        self.order(root, depth, res)
        return root