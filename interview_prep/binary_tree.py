class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return None

        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result

def preorderTraversal(root: TreeNode):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return None

        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result



def postorderTraversal(root: TreeNode):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return None

        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


from collections import deque
def levelTraversal(root: TreeNode):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(level)
            
            
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)


print("Preoder traversal: ", preorderTraversal(root))
print("Inorder traversal: ", inorderTraversal(root))
print("Postorder traversal: ", postorderTraversal(root))
print("Level Order traversal: ", levelTraversal(root))