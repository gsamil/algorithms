class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Prints the tree as a list joined by space, BFS order"""
        if self is None:
            return ""
        queue = [self]
        result = []
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append("null")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(result)
