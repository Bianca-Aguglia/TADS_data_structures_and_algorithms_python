#!usr/bin/python
'''
Implementation of stack in Python.
'''

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f'Node({self.value})'
    
    def __str__(self):
        if self.next:
            return f'Node(value: {self.value}, next: {self.next.value})'
        return f'Node(value: {self.value}, next: None)'
    
class Stack:
    def __init__(self, value = None):
        if value:
            self.top = Node(value)
        else:
            self.top = None
        
    def __repr__(self):
        elements = []
        cursor = self.top
        while cursor:
            if cursor.value:
                elements.append(str(cursor.value))
            cursor = cursor.next
        if elements:
            elements.append('None')
            return ' -> '.join(elements)
        return 'stack is empty'

    def __str__(self):
        elements = []
        cursor = self.top
        while cursor:
            if cursor.value:
                elements.append(str(cursor.value))
            cursor = cursor.next
        if elements:
            elements.append('None')
            return ' -> '.join(elements)
        return 'stack is empty'

    
    def push(self, value):
        if self.top:
            self.top, self.top.next = Node(value), self.top
        else:
            self.top = Node(value)
            
    def pop(self):
        if self.top:
            popped = self.top.value
            self.top = self.top.next
            return popped
        return 'stack is empty'
    
    def peek(self):
        if self.top:
            return self.top.value
        return 'stack is empty'
    
    def is_empty(self):
        return not self.top    

    