# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        """
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        """
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        """
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        """
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below


def pre_order_recursive(root: TreeNode) -> None:
    # Your code goes here
    if root is None:
        return
    print(root.value)
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    if root is None:
        return

    stack = [root]

    while len(stack) > 0:
        node = stack.pop()
        print(node.value)
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)


def in_order_recursive(root: TreeNode) -> None:
    pass


def post_order_recursive(root: TreeNode) -> None:
    pass


def breadth_first(root: TreeNode) -> None:
    pass


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    # Your code goes here


def graph_depth_first_iterative(node: GraphNode) -> None:
    pass


def graph_breadth_first(node: GraphNode) -> None:
    pass
