class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this, not_rob_this)

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob this node → cannot rob children
            rob_this = node.val + left[1] + right[1]

            # Do not rob this node → free to rob children
            not_rob_this = max(left) + max(right)

            return (rob_this, not_rob_this)

        return max(dfs(root))
