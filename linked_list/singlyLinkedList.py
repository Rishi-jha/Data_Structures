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
        return str(self.value)

    def show(self):
        while self.next:
            self.next.show()
            print(self.value,end=">")

class SinglyLinkedList(object):
    '''
    Linked List
    '''

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value, index=None):
        if index is None:
            self.insert_at_end(value)
        else:
            self.insert_at_index(value, index)
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_at_end(self, value):
        if self.head:
            self.head.insert(value)
        else:
            self.head = Node(value)
        self.length += 1

    def insert_at_index(self, value, index):
        if self.length <= index:
            raise IndexError("You are trying to insert at index which is not available.\nLenght of List is {0}, your index: {1}".format(self.length, index))
        head = self.head
        if index == 0:
            print(index)
            self.head = Node(value)
            self.head.next = head
        else:
            print("asa")
            starting = 0
            while head.next:
                if starting >= index:
                    break
                head = head.next
                starting += 1

            head_next = head.next
            head.next = Node(value)
            head.next.next = head_next
            self.length += 1

    def __str__(self):
        return "SinglyLinkedList({})".format([eval(str(i)) for i in self])

    def __len__(self):
        return self.length

    def show(self, sep="-->"):
        head = self.head
        for i in range(0,self.length):
            if i != 0:
                print(end=sep)
            print(head.value,end="")
            head = head.next
        print()



