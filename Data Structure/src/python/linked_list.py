from pydantic import BaseModel
from typing import Any


class Node(BaseModel):
    data: Any = None
    next: Any = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __is_empty(self):
        if self.head is None:
            return True
        return False

    def add_node(self, data):
        """
        Create new node
        check if head is empty
            if empty set new node as head of linked list
            else set next of new node to head and set new node as head of linked list
        """
        new_node = Node(data=data)
        if self.__is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return True

    def add_node_at_end(self, data):
        """
        Add node at end of linked list

        approach:
        - create new node
        - check if head is none
            - if none set new node as head
            - else iterate over linked list till last node
            - set next of last node to new node and set new node next as none
        """

        new_node = Node(data=data)
        if self.__is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.next = None

        return True

    def add_node_at_position(self, data, index):
        """
        Add node at given position

        approach:
        - create new node
        - check if index == 0 if yes then call add_node method
        - iterate over linked list till index-1
        - update next of new node to next of current node
        - update next of current node to new node
        """
        if index == 0:
            return self.add_node(data)

        position = 0  # It will keep track of current index
        new_node = Node(data=data)
        current = self.head

        while current is not None and position + 1 != index:  # Iterate till index-1
            current = current.next
            position += 1

        # Index out of bound
        if current is None:
            return False

        # Updating the ll logic
        new_node.next = current.next
        current.next = new_node
        return True

    def update_node(self, data, index):
        """
        Update node at given index

        approach
        check if linked list is empty
        iterate over linked list till index
        update data of current node
        """

        # Empty linked list condition
        if self.__is_empty():
            return False

        # Update node
        current = self.head
        position = 0
        while current is not None and position != index:
            current = current.next
            position += 1

        # Index out of bound
        if current is None:
            return False

        current.data = data

        return True

    def remove_first_node(self):
        if self.__is_empty():
            return False
        self.head = self.head.next
        return True

    def remove_last_node(self):
        return

    def remove_node_at_position(self, index):
        return

    def search_by_value(self, data):
        return

    def print_ll(self):
        """
        print all nodes of linked list

        Approach:
        - store head in a variable
        - iterate over linked list current is none
        - print data of current node
        """

        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

        print()


if __name__ == "__main__":
    ll = LinkedList()

    print("Checking if linked list is empty")
    assert ll.head is None

    print("Adding new nodes")
    assert ll.add_node(1) == True
    assert ll.add_node(2) == True
    assert ll.add_node(3) == True

    ll.print_ll()

    print("Adding new node at end")
    assert ll.add_node_at_end(4) == True

    print("Adding new node at position")
    assert ll.add_node_at_position(2.1, 2) == True

    print("Adding new node at position not present in ll")
    assert ll.add_node_at_position(5.1, 12) == False

    ll.print_ll()
