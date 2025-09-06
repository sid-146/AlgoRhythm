from typing import List


class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def pre_order(root: Node):
    # root, left, right
    stack: List[Node] = [root]

    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    pre_order(root)


main()
