class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def in_order(root: Node):
    # left, root, right

    if root is None:
        return

    in_order(root.left)
    print(root.value, end=" ")
    in_order(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    in_order(root)

    # print_tree_pyramid(root)


main()
