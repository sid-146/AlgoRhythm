from typing import List


class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def in_order(root: Node):
    # Todo: incomplete
    # left,root, right
    if root is None:
        return

    stack: List[Node] = []
    node = root

    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                # i have traversed the whole tree
                break
            node = stack.pop()
            print(node.value, end=" ")
            node = node.right


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    in_order(root)


main()
