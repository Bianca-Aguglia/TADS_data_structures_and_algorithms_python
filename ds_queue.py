#!usr/bin/python
'''
Implementation of queue data structure
'''

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
            return f'Node(value: {self.value}, next: None)'
        
class Queue:
    def __init__(self, value=None):
        if value:
            self.front = self.rear = Node(value)
        else:
            self.front = self.rear = None
            
    def enqueue(self, value):
        node = Node(value)
        
        if self.rear == None:
            self.front = self.rear = node
            return
        
        self.rear.next = node
        self.rear = node
        
    def dequeue(self):
        if self.is_empty():
            return 'queue is empty'
        
        dequeued = self.front.value
        self.front = self.front.next
        
        if self.is_empty():
            self.rear = None
            
        return dequeued
        
    def is_empty(self):
        return not self.front
    
    def __repr__(self):
        nodes = []
        cur = self.front
        while cur:
            nodes.append(str(cur.value))
            cur = cur.next
        nodes.append('None')
        nodes.reverse()
        return ' <- '.join(nodes)
    
    def __str__(self):
        nodes = []
        cur = self.front
        while cur:
            nodes.append(str(cur.value))
            cur = cur.next
        nodes.append('None')
        nodes.reverse()
        return ' <- '.join(nodes)   