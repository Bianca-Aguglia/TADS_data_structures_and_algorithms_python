#!usr/bin/python
#implementation of linked lists in python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f'Node({self.value})'
        
    def __str__(self):
        try: 
            return f'Node(value: {self.value}, next: {self.next.value})'
        except:
            return f'Node(value: {self.value}, next: {self.next})'
        
class LinkedList:
    def __init__(self, value = None):
        if value:
            self.head = Node(value)
        else:
            self.head = None
            
    def __iter__(self):
        node = self.head
        while node:
            try:
                yield (node.value, node.next.value)
            except:
                yield (node.value, node.next)
            node = node.next

    def __str__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def append(self, value):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert(self, new_node, existing_node):
        node = self.head
        new_node = Node(new_node)
        while node.next:
            if node.next.value == existing_node:
                new_node.next = node.next
                node.next = new_node
                return f'node {new_node.value} inserted'
            node = node.next
        return f'node {existing_node} is not in the linked list'
                
    def remove(self, node):
        cur_node = self.head
        # if node to be removed is self.head
        if cur_node.value == node:
            self.head = cur_node.next
            return
        while cur_node.next:
            if cur_node.next.value == node:
                cur_node.next.next = None
                cur_node.next = cur_node.next.next
                return f'node {node} deleted'
            cur_node = cur_node.next
        return f'node {node} is not in the linked list'
        