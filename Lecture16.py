# Lecture 16

'''
Binary Tree Implementation
- Recall: A Binary Tree is a tree structure where a node has at most two children
- So far, we've talked about binary trees on a conceptual level (heaps, and
  analyzing sorting algorithms like merge sort and quick sort).
- We even talked about Binary Heaps that can be conceptualized as a complete
  binary tree
      - And there are many ways to implement trees!
'''

'''
Nodes and References Representation
- Similar to our Linked List representation, we can expand upon this concept
  using nodes and references to construct our tree
- Each node can be represented as an object
    - Each Node will have left/right child references to other nodes in the tree
    - Each Node is the root of its own subtree
'''

class BinaryTreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    
    def insertLeft(self, newNode):
        # Case 1: Node does not have a left child
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a left child
            t = BinaryTreeNode(newNode)
            t.leftChild = self.leftChild # Links the left sub tree
            self.leftChild = t

    def insertRight(self, newNode):
        # Case 1: Node does not have a right child
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a right child
            t = BinaryTreeNode(newNode)
            t.rightChild = self.rightChild # Links the right sub tree
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key


# pytests
def test_createNode():
    node = BinaryTreeNode("A")
    assert node.getRootValue() == "A"
    assert node.getLeftChild() == None
    assert node.getRightChild() == None

def test_leftNode():
    node = BinaryTreeNode("A")
    node.insertLeft("B")
    assert node.getRootValue() == "A"
    assert node.getLeftChild().getRootValue() == "B"
    assert node.getRightChild() == None
    assert node.getLeftChild().getLeftChild() == None
    assert node.getLeftChild().getRightChild() == None

def test_rightNode():
    node = BinaryTreeNode("A")
    node.insertRight("B")
    assert node.getRightChild().getRootValue() == "B"
    assert node.getRootValue() == "A"
    assert node.getLeftChild() == None
    assert node.getRightChild().getLeftChild() == None
    assert node.getRightChild().getRightChild() == None

def test_insertLeft():
    node = BinaryTreeNode("A")
    node.insertLeft("B")
    node.insertLeft("C")
    node.insertLeft("D")

    temp = node
    s = ''
    while temp != None:
        s = s + temp.getRootValue()
        temp = temp.getLeftChild()
        
    assert s == "ADCB"

'''
Tree Traversals
- Sometimes, we want to visit ALL nodes in a binary tree
- We can do this in various ways, and the order of visiting the nodes may vary
- There are three common recursive ways to traverse nodes in a tree
    1. preorder
        - Visit the node first, then recursively go down left subtree, then
          recursively go down right subtree
    2. inorder
        - Recursively go down left subtree, visit the node, then recursively go
          down right subtree
    3. postorder
        - Recursively go down left subtree, then recursively go down right subtree,
          then visit the node
'''

def preorder(tree):
    ret = ""
    if tree != None:
        ret += tree.getRootValue() # visit node
        ret += preorder(tree.getLeftChild())
        ret += preorder(tree.getRightChild())
    return ret

def inorder(tree):
    ret = ""
    if tree != None:
        ret += inorder(tree.getLeftChild())
        ret += tree.getRootValue()
        ret += inorder(tree.getRightChild())
    return ret

def postorder(tree):
    ret = ""
    if tree != None:
        ret += postorder(tree.getLeftChild())
        ret += postorder(tree.getRightChild())
        ret += tree.getRootValue()
    return ret


# pytests    
def test_preorder():
    # Create Tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert preorder(root) == "ABDCEF"    

def test_inorder():
    # Create tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert inorder(root) == "DBAECF"

def test_postorder():
    # Create tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.insertRight("C")
    root.getRightChild().insertLeft("E")
    root.getRightChild().insertRight("F")
    assert postorder(root) == "DBEFCA"

'''
Binary Search Tree (BST)
- Binary SEARCH Tree are binary trees that have the following properties:
    - Values that are less than the parent are found in the left subtree
    - Values that are greater than the parent are found in the right subtree
    - This is known as the BST property
- Binary Search Tree is one way to implement a MAP Abstract Data Type
    - A Map ADT maps keys to corresponding values
    - Think of keys defining where in the BST structure a node gets inserted
    - And each node has a corresponding value field
    - Similar to how Python Dictionaries work on a high-level
      (but the underlying implementation between a Python Dictionary and BST
      are different (each with pros / cons))
- Note: Insertion order of elements affects the structure of the tree!
- Also note: inorder traversal in a BST will visit the nodes in order
'''
