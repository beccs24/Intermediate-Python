# Lecture 18/19

'''
BST Deletion
Cases:
1. When the node to be deleted is a leaf node (has no children)
- Find the node that needs to be deleted
- Simply remove the parent reference (either left child or right child) to the deleted node

2. When the node to be deleted has 1 child
- Find the node that needs to be deleted
- Connect the deleted node's parent reference and the deleted node's child reference together

3. When the node to be deleted has 2 children
- Find the node that needs to be deleted
- Find the node's successor - the next greatest node value (in the right subtree for BST maintenance)
    - This can be done by traversing the left children of the node to be deleted’s right subtree
    - Also note that the successor will always only have at most one child
        - If the successor had a left child, then it wouldn’t be the successor!
- Temporarily store the successor and delete the successor from the tree
    - Delete the successor from the tree (Case 1 or Case 2)
- Replace node to be deleted value with the successor's value
'''

implementation in Lecture17

    


