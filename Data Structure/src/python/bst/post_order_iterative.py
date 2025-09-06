from typing import List


class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def post_order(root):
    # left, right, root
    answers: List[int] = []
    traverse_stack: List[Node] = [root]

    while traverse_stack:
        node = traverse_stack.pop()
        if node is None:
            return

        answers.append(node.value)
        if node.left is not None:
            traverse_stack.append(node.left)
        if node.right is not None:
            traverse_stack.append(node.right)

    return answers


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(post_order(root)[::-1])


main()
