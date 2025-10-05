# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cameras = 0

        def dfs(node):
            if not node:
                return 1  # 空节点视为已被覆盖（无需相机）

            left = dfs(node.left)
            right = dfs(node.right)

            # 若任一子节点未被覆盖，则此节点必须装摄像头
            if left == 0 or right == 0:
                self.cameras += 1
                return 2
            # 若任一子节点装有摄像头，则该节点被覆盖
            elif left == 2 or right == 2:
                return 1
            # 否则，此节点未被覆盖
            else:
                return 0

        # 根节点若未被覆盖，再加一个摄像头
        if dfs(root) == 0:
            self.cameras += 1
        return self.cameras
