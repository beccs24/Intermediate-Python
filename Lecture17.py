# Lecture 17

# TreeNode
class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        # considers None as a False value
        return self.leftChild 

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self

        if self.hasRightChild():
            self.rightChild.parent = self

    # This implementation is for BST maintenance (not the general case)
    def findSuccessor(self):
        succ = None
        # Check if node has a right subtree
        if self.hasRightChild():
            # traverse through the left children
            succ = self.rightChild.findMin()
        return succ

    # Find the minimum value in a subtree by walking down the left children
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
        
    def spliceOut(self, ):
        # Case 1
        # If node to be removed is the leaf, set parent's left or right child
        # references to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
                
        # Case 2
        # Not a leaf node. Should only have a right child for BST maintenance
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parents

# BinarySearchTree
class BinarySearchTree:
    def __init__(self):
        self.root = None # A BST just needs a reference to the root node
        self.size = 0 # Keeps track of number of nodes

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    # helper method to recursively walk down the tree
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self,key): # returns payload for key if it exists
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    # helper method to recursively walk down the tree
    def _get(self, key, currentNode): 
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)



    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # remove modifies the tree
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    # Used to remove the node and account for BST deletion cases
    def remove(self, currentNode):
        # Case 1: Node to remove is leaf
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
                
        # Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            # Need to find the successor, remove successor, and replace
            # currentNode with the successor's data/payload
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            
        # Case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            # Node has rightChild
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


    def sumChildrenKeys(self, keyItem):
        if self.root:
            currentNode = self._get(keyItem, self.root)
            if currentNode:
                if currentNode.isLeaf():
                    return 0
                elif currentNode.hasBothChildren():
                    leftval = currentNode.leftChild.key
                    rightval = currentNode.rightChild.key
                    return leftval + rightval
                else:
                    if currentNode.hasLeftChild():
                        return currentNode.leftChild.key
                    else:
                        return currentNode.rightChild.key
            else:
                return None
        else:
            return None
        
        
    def descendingInOrder(self, currentNode):
        ret = []
        if currentNode != None:
            ret += self.descendingInOrder(currentNode.rightChild)
            ret += [currentNode.key]
            ret += self.descendingInOrder(currentNode.leftChild)
        return ret
                                    

##        ret = []
##        if currentNode != None:
##            ret.insert(0, (self.descendingInOrder(currentNode.leftChild)))
##            ret.insert(0, currentNode.key)
##            ret.insert(0, (self.descendingInOrder(currentNode.rightChild)))
##        return ret
        
    
    # Used for pytesting
    def inOrder(self, node):
        ret = ''
        if node != None:
            ret += self.inOrder(node.leftChild)
            ret += str(node.key) + ' '
            ret += self.inOrder(node.rightChild)
        return ret

    def preOrder(self, node):
        ret = ''
        if node != None:
            ret += str(node.key) + ' '
            ret += self.inOrder(node.leftChild)
            ret += self.inOrder(node.rightChild)
        return ret

'''
# pytest
def test_constructBST():
    BST = BinarySearchTree()
    assert BST.root == None
    assert BST.length() == 0

# test for put
def test_insertRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.root.key == 10
    assert BST.root.payload == "ten"
    assert BST.root.hasLeftChild() == None
    assert BST.root.hasRightChild() == None
    assert BST.root.isLeftChild() == None
    assert BST.root.isRightChild() == None
    assert BST.root.isRoot() == True
    assert BST.root.hasAnyChildren() == None
    assert BST.root.isLeaf() == True
    assert BST.root.hasBothChildren() == None
    BST.root.replaceNodeData(20, "twenty", None, None)
    assert BST.root.key == 20
    assert BST.root.payload == "twenty"

def test_insertNodes():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    assert BST.root.key == 10
    assert BST.root.leftChild.key == 5
    assert BST.root.rightChild.key == 20
    assert BST.root.rightChild.leftChild.key == 15

def test_deleteSingleRoot():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    assert BST.inOrder(BST.root) == '10 '
    BST.delete(10)
    assert BST.size == 0
    assert BST.root == None

def test_deleteRootOneChild():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    BST.put(5, 'five')
    assert BST.inOrder(BST.root) == '5 10 '
    BST.delete(10)
    assert BST.inOrder(BST.root) == '5 '
    assert BST.root.key == 5

def test_deleteLeaf():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    BST.put(15, 'fifteen')
    BST.put(5, 'five')
    BST.put(2, 'two')
    assert BST.inOrder(BST.root) == '2 5 10 15 '
    BST.delete(15)
    assert BST.inOrder(BST.root) == '2 5 10 '

def test_deleteNodeOneChild():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    BST.put(15, 'fifteen')
    BST.put(5, 'five')
    BST.put(2, 'two')
    assert BST.root.leftChild.key == 5
    BST.delete(5)
    assert BST.inOrder(BST.root) == '2 10 15 '
    assert BST.root.leftChild.key ==  2
    assert BST.root.leftChild.parent.key == 10
    
def test_deleteRootWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    BST.put(15, 'fifteen')
    BST.put(5, 'five')
    BST.put(3, 'three')
    BST.put(7, 'seven')
    BST.put(12, 'twelve')
    BST.put(17, 'seventeen')
    assert BST.inOrder(BST.root) == '3 5 7 10 12 15 17 '
    BST.delete(10)
    assert BST.inOrder(BST.root) == '3 5 7 12 15 17 '

def test_deleteNodeWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, 'ten')
    BST.put(15, 'fifteen')
    BST.put(5, 'five')
    BST.put(3, 'three')
    BST.put(7, 'seven')
    BST.put(12, 'twelve')
    BST.put(17, 'seventeen')
    BST.delete(15)
    assert BST.inOrder(BST.root) == '3 5 7 10 12 17 '
    BST.delete(5)
    assert BST.inOrder(BST.root) == '3 7 10 12 17 '
'''
'''
def test_sumChildrenKeys():
    BST1 = BinarySearchTree()
    BST1.put(5, "five")
    BST1.put(4, "four")
    BST1.put(1, "one")
    BST1.put(10, "ten")
    BST1.put(3, "three")
    BST1.put(6, "six")
    BST1.put(9, "nine")
    BST1.put(12, "twelve")
    BST1.put(11, "eleven")
    BST1.put(13, "thirteen")
    assert BST1.sumChildrenKeys(5) == 14
    assert BST1.sumChildrenKeys(4) == 1
    assert BST1.sumChildrenKeys(12) == 24
    assert BST1.sumChildrenKeys(10) == 18
    assert BST1.sumChildrenKeys(9) == 0
    assert BST1.sumChildrenKeys(100) == None
    assert BST1.sumChildrenKeys(2) == None
'''
    

BST1 = BinarySearchTree()
assert BST1.descendingInOrder(BST1.root) == []
BST1.put(5, "five")
BST1.put(4, "four")
BST1.put(1, "one")
BST1.put(10, "ten")
print(BST1.descendingInOrder(BST1.root))
#assert BST1.descendingInOrder(BST1.root) == [10,5,4,1]
BST1.put(3, "three")
BST1.put(6, "six")
BST1.put(9, "nine")
BST1.put(12, "twelve")
BST1.put(11, "eleven")
BST1.put(13, "thirteen")
#assert BST1.descendingInOrder(BST1.root) == [13,12,11,10,9,6,5,4,3,1]

def test_descendingInOrder():
    BST1 = BinarySearchTree()
    assert BST1.descendingInOrder(BST1.root) == []
    BST1.put(5, "five")
    BST1.put(4, "four")
    BST1.put(1, "one")
    BST1.put(10, "ten")
    BST1.descendingInOrder(BST1.root)
    assert BST1.descendingInOrder(BST1.root) == [10,5,4,1]
    BST1.put(3, "three")
    BST1.put(6, "six")
    BST1.put(9, "nine")
    BST1.put(12, "twelve")
    BST1.put(11, "eleven")
    BST1.put(13, "thirteen")
    assert BST1.descendingInOrder(BST1.root) == [13,12,11,10,9,6,5,4,3,1]
