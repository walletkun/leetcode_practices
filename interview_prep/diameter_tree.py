class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def diameterTree(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1

    dfs(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(diameterTree(root))