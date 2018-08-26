#!/usr/bin/env python
'''
Singly linked list are the list having nodes with each node have a pointer for the next element.
'''

#Definition of each node
class Node(object):
    '''
    Node Class
    '''

    def __init__(self, value):
        """
        """
        self.value = value
        self.next = None

    def insert(self, value):
        if self.next:
            self.next.insert(value)
        else:
            self.next = Node(value)

    def __str__(self):
        return "Node({})".format(self.value)

    def __repr__(self):
        return "Node({})".format(self.value)

    def show(self):
        while self.next:
            self.next.show()
            print(self.value, end=">")

class SinglyLinkedList(object):
    '''
    Singly Linked List Class
    '''

    def __init__(self):
        """
        Constructor for SinglyLinkedList Class
        """
        self.head = None
        self.length = 0

    def insert(self, value, index=None):
        """
        Method to insert in a linked list, you can optionally provide index.
        If index is not provided it will append new node at the end.
        insert(value,[index])
        :param: value: Value to be inserted inside the SinglyLinkedList
        :type: value: Object
        :param: index: Optional Index attribute to insert at certain index
        :type: index: int
        :raises: IndexError if index provided is greater than the length of SinglyLinkedList
        :rtype: None
        """
        if index is None:
            self._insert_at_end(value)
        else:
            self._insert_at_index(value, index)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def _insert_at_end(self, value):
        """
        Intermediate method to add a node to end.
        :param: value: Value to add
        :type: value: object
        """
        if self.head:
            self.head.insert(value)
        else:
            self.head = Node(value)
        self.length += 1

    def _insert_at_index(self, value, index):
        """
        Intermediate method to add a node to end.
        :param: value: Value to add
        :type: value: object
        :param: index: Index to add
        :type: index: int
        """
        if self.length <= index:
            raise IndexError("You are trying to insert at index which is not available.\nLenght of List is {0}, your index: {1}".format(self.length, index))
        head = self.head
        if index == 0:
            self.head = Node(value)
            self.head.next = head
        else:
            starting = 0
            while head.next:
                if starting == index-1:
                    break
                head = head.next
                starting += 1

            head_next = head.next
            head.next = Node(value)
            head.next.next = head_next
            self.length += 1

    def __str__(self):
        return "SinglyLinkedList({})".format([eval(str(i)) for i in self])

    def __repr__(self):
        return "SinglyLinkedList({})".format([eval(str(i)) for i in self])

    def __len__(self):
        return self.length

    def show(self, sep="-->"):
        """
        Print the complete list in order.
        :param: sep: Optional Separator: default: -->
        :type: sep: str
        :rtype: None
        """
        print("{}".format(sep).join([str(item.value) for item in self]))
    
    def remove(self,index=0):
        """
        Method for removing a Node in the SinglyLinkedList
        :param: index: Index of the node which you want to delete.
        :type: index: int
        :rtype: None
        :raises ValueError: If trying to delete from an empty list
        :raises IndexError: If trying to delete which does not exist.
        """
        if not self.length:
            raise ValueError("Cannot delete from an empty Linked List")
        if not index:
            self.head = self.head.next
            self.length -= 1
        else:
            self._remove_at_index(index+1)

    def _remove_at_index(self, index):
        counter = 0
        curr_node = self.head
        prev_node = self.head
        if not (0 < index or index < self.length):
            raise IndexError("Index you provided does not exist")
        while curr_node.next != None or counter < index:
            counter += 1
            if counter == index:
                prev_node.next = curr_node.next
                self.length -= 1
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def _remove_at_start(self):
        self.head = self.head.next
        self.length -= 1
