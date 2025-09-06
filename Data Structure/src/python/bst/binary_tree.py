from collections import deque


class Node:
    def __init__(self, value: int):
        self.left: "Node" = None
        self.right: "Node" = None
        self.value: int = value


def print_tree_pyramid(root: Node):
    if not root:
        return

    # BFS traversal to get levels
    q = deque([(root, 0)])
    levels = {}
    max_level = 0

    while q:
        node, level = q.popleft()
        if level not in levels:
            levels[level] = []
        levels[level].append(node.value if node else None)
        max_level = max(max_level, level)

        if node:
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

    # Print levels with spacing
    max_width = int(pow(2, max_level)) * 4
    for level in range(max_level + 1):
        values = levels[level]
        spacing = int(max_width / (len(values) + 1))
        line = ""
        for v in values:
            line += " " * spacing
            line += str(v) if v is not None else " "
        print(line)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print_tree_pyramid(root)


main()
