from sys import stdin
from copy import deepcopy

class Node(object):
    def __init__(self, key, left=None, right=None):
        self._key = key
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left
        
    @property
    def right(self):
        return self._right
        
    @property
    def key(self):
        return self._key
        
class Tree(object):
    def __init__(self, tree_dict):
        self._tree_dict = tree_dict
        self._root = self._create_tree('A')

    def _create_tree(self, node_key):
        left, right = self._tree_dict.get(node_key)

        left_node = None
        right_node = None
        if left != '.':
            left_node = self._create_tree(left)
        if right != '.':
            right_node = self._create_tree(right)

        return Node(node_key,
                    deepcopy(left_node),
                    deepcopy(right_node))

    def preorder_traverse(self):
        return self._preorder_traverse(self._root)
    
    def _preorder_traverse(self, node):
        if node is None:
            return ''
        return ''.join([node.key,
                        self._preorder_traverse(node.left), 
                        self._preorder_traverse(node.right)])

    def inorder_traverse(self):
        return self._inorder_traverse(self._root)
    
    def _inorder_traverse(self, node):
        if node is None:
            return ''
        return ''.join([self._inorder_traverse(node.left),
                        node.key,
                        self._inorder_traverse(node.right)])

    def postorder_traverse(self):
        return self._postorder_traverse(self._root)
    
    def _postorder_traverse(self, node):
        if node is None:
            return ''
        return ''.join([self._postorder_traverse(node.left),
                        self._postorder_traverse(node.right),
                        node.key])


if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    tree_dict = {}
    for _ in range(n):
        k, l, r = stdin.readline().rstrip().split(' ')
        tree_dict[k] = (l, r)

    t = Tree(tree_dict)
    print(t.preorder_traverse())
    print(t.inorder_traverse())
    print(t.postorder_traverse())
    
