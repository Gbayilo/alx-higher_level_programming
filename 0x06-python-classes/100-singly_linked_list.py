#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data of the Node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node.

        Args:
            value (Node): The new next_node.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self._head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The data for the new Node.
        """
        new_node = Node(value)
        if self._head is None or self._head.data > value:
            new_node.next_node = self._head
            self._head = new_node
        else:
            tmp = self._head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self._head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
