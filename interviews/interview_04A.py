class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_leftmost_child(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node


def in_order_succ(node: TreeNode) -> TreeNode:
    if not node:
        return None

    # Are there any right children?
    if node.right:
        # If so, return the leftmost child of the right subtree
        return get_leftmost_child(node.right)

    # If not, we need to go up the tree until we find a node that is the left child of its parent
    while node.parent and node.parent.right == node:
        node = node.parent

    if not node.parent:
        return None

    return node.parent
