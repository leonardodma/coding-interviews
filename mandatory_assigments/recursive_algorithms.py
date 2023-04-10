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
            self.root = None
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


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node


# Implement the functions below


def list_sum(l: list[int]) -> int:
    if len(l) == 0:
        return 0

    return l.pop() + list_sum(l)


def digit_sum(n: int) -> int:
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


def tree_sum(root: TreeNode) -> int:
    if root is None:
        return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root: TreeNode) -> int:
    if root is None:
        return -float("inf")

    return max(root.value, tree_max(root.left), tree_max(root.right))


def k_combinations(l: list[int], k: int) -> list[list[int]]:
    if k == 0:
        return [[]]

    if len(l) == 0:
        return []

    return [[l[0]] + x for x in k_combinations(l[1:], k - 1)] + k_combinations(l[1:], k)


def all_strictly_increasing_sequences(k: int, n: int, **kwargs) -> list[list[int]]:
    if k == 0:
        return [[]]

    if n == 0:
        return []

    start = kwargs["start"] if "start" in kwargs else 0

    result = []
    for i in range(start + 1, n + 1):
        for x in all_strictly_increasing_sequences(k - 1, n, start=i):
            seq = [i] + x
            result.append(seq)

    return result


def create_pattern(n: int, reach_negative=False, original=None) -> list[int]:
    if original is None:
        original = n

    if n == 0 and original == 0:
        return [0]

    if n == original and reach_negative:
        return [n]

    if n <= 0 and not reach_negative:
        reach_negative = True

    return (
        [n] + create_pattern(n - 5, reach_negative, original)
        if not reach_negative
        else [n] + create_pattern(n + 5, reach_negative, original)
    )


def find_middle(head: LinkedListNode) -> LinkedListNode:
    # Don't change this function
    result = find_middle_rec(head)
    return result[1]


def find_middle_rec(head: LinkedListNode, n: int = 0) -> tuple[int, LinkedListNode]:
    # Hint: n will be used to count nodes from left to right and
    # the number returned by the function will be used to count the nodes from right to left

    if head is None:
        return n // 2, None

    count, node = find_middle_rec(head.next, n + 1)

    if count == n:
        return count, head

    return count, node
