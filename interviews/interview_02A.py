from typing import Tuple


""" class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt """


def get_linked_list_tail_and_size(head):
    """Get the tail and size of a linked list."""

    size = 1

    current_node = head
    while current_node.next is not None:
        size += 1
        current_node = current_node.next

    return current_node, size


def find_intersection(head1, head2):
    """Find the intersection of two linked lists, if exists."""
    if head1 is None or head2 is None:
        return None

    tail_ll_1, size_ll_1 = get_linked_list_tail_and_size(head1)
    tail_ll_2, size_ll_2 = get_linked_list_tail_and_size(head2)

    if tail_ll_1 is not tail_ll_2:
        return None

    # Sync two linked lists pointer
    must_advance = size_ll_1 - size_ll_2
    current_node_ll_1 = head1
    current_node_ll_2 = head2

    while must_advance != 0:
        if must_advance > 0:
            current_node_ll_1 = current_node_ll_1.next
            must_advance -= 1
        else:
            current_node_ll_2 = current_node_ll_2.next
            must_advance += 1

    while current_node_ll_1 is not current_node_ll_2:
        current_node_ll_1 = current_node_ll_1.next
        current_node_ll_2 = current_node_ll_2.next

    return current_node_ll_1
