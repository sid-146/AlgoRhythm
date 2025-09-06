from typing import Deque

from collections import deque


class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def breadth_first_search(root):
    queue: Deque[Node] = deque([root])
    answer = []

    while queue:
        node = queue.popleft()
        answer.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return answer


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(breadth_first_search(root))


main()
