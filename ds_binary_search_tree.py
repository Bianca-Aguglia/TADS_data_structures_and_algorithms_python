class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f'Node({self.value})'
        
    def __str__(self):
        try:
            return f'Node(value: {self.value}, left: {self.left.value}, right: {self.right.value})'
        except: # if node is root node
            return f'Node(value: {self.value}, left: {self.left}, right: {self.right})'
        
class BST:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return f'root created: {value}'
        else:
            ins = self._insert(self.root, value)
            return ins
            
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return f'{value} was inserted in tree'
            else:
                return self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return f'{value} was inserted in tree'
            else:
                return self._insert(node.right, value)
        else:
            return f'{value} already in tree'
        
    def print_tree(self, traversal_type='in_order'):
        if traversal_type == 'in_order':
            return self.print_in_order(self.root)
        elif traversal_type == 'pre_order':
            return self.print_pre_order(self.root)
        elif traversal_type == 'post_order':
            return self.print_post_order(self.root)
        else:
            return f'{traversal_type} traversal type not supported'
        
                
    def print_in_order(self, node):
        nodes = []
        if node:
            nodes.extend(self.print_in_order(node.left))
            nodes.append(node.value)
            nodes.extend(self.print_in_order(node.right))
        return nodes
        
    def print_pre_order(self, node):
        nodes = []
        if node:
            nodes.append(node.value)
            nodes.extend(self.print_pre_order(node.left))
            nodes.extend(self.print_pre_order(node.right))
        return nodes
    
    def print_post_order(self, node):
        nodes = []
        if node:
            nodes.extend(self.print_post_order(node.left))
            nodes.extend(self.print_post_order(node.right))
            nodes.append(node.value)
        return nodes
    
    def search(self, value):
        if self.root:
            return self._search(self.root, value)
        else:
            return 'tree is empty'
    
    def _search(self, node, value):
        if node:
            if node.value == value:
                return True
            elif value < node.value:
                return self._search(node.left, value)
            elif value > node.value:
                return self._search(node.right, value)
        else:
            return False
        
    def find_max(self):
        if self.root is None:
            return 'tree is empty'
        else:
            cur_node = self.root
            while cur_node.right:
                cur_node = cur_node.right
            return cur_node.value
        
    
    def find_min(self, value):
        if self.root is None:
            return 'tree is empty'
        else:
            cur_node = self.root
            while cur_node.left:
                cur_node = cur_node.left
            return cur_node.value
    
    def find_closest(self, value):
        if self.root is None:
            return 'tree is empty'
        else:
            cur_diff = abs(self.root.value - value)
            cur_val = self.root.value
            return self._find_closest(self.root, cur_diff, cur_val, value)
        
    def _find_closest(self, cur_node, cur_diff, cur_val, value):
        if cur_node:
            if abs(cur_node.value - value) < cur_diff:
                cur_diff = abs(cur_node.value - value)
                cur_val = cur_node.value
            if value < cur_node.value:
                return self._find_closest(cur_node.left, cur_diff, cur_val, value)
            elif value > cur_node.value:
                return self._find_closest(cur_node.right, cur_diff, cur_val, value)
        cur_closest = {'minimum_difference': cur_diff,
                      'closest_value': cur_val}
        return cur_closest
            
            
    
    def remove(self, value):
        if self.root is None:
            return 'tree is empty'
        if not self.search(value):
            return 'value not in tree'
        return self._remove(self.root, value)
    
    def _remove(self, node, value):
        if value < node.value:
            # target value is in left subtree
            node.left = self._remove(node.left, value)
            return f'{value} was removed from tree'
        
        elif value > node.value:
            # target value is in right subtree
            node.right = self._remove(node.right, value)
            return f'{value} was removed from tree'
        
        else:
            # found target value
            if node.left == node.right == None:
                return None
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left
            parent, replacement_node = node, node.left
            while replacement_node.right is not None:
                parent, replacement_node = replacement_node, replacement_node.right
            # Now, `node` is the rightmost node in the left subtree, and
            # `parent` its parent node. Instead of replacing `self`, we change
            # its attributes to match the value of `node`.
            if parent.left is replacement_node:
                # This check is necessary, because if the left subtree has only
                # node, `node` would be `self.left`.
                parent.left = None
            else:
                parent.right = None
            node.value = replacement_node.value
            return node    