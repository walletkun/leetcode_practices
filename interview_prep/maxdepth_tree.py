"""
Problem: Max Depth of Binary Tree
Description:
Given the root of a binary tree, return its maximum depth — the number of nodes along the longest path from the root down to the farthest leaf node.

Example:
Input:

    1
   / \
  2   3
 / \
4   5
Longest path is: 1 → 2 → 4 or 1 → 2 → 5

Max depth = 3
"""

class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    def dfs(node, depth):
        if not node:
            return depth

        left = dfs(node.left, depth + 1)
        right = dfs(node.right, depth + 1)

        return max(left, right)

    return dfs(root, 0)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(maxDepth(root))