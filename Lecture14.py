# Lecture 14

'''
Quicksort
- Another divide and conquer algorithm
- Can improve running times to O(n logn) (like mergesort) in a TYPICAL case, but
  we'll see how this can lead to O(n^2) in a worst-case scenario.
- BUT, Quicksort does not need additional memory

- Idea: Can sort a list by subdividing the list based on a PIVOT value
    - Place elements < pivot to the left-side of the list
    - Place elements > pivot to the right-side of the list
    - Recurse for each left/right portion of the list
    - When sublist sizes == 1, we're done

- HOW do we partition the list into left/right sublists?
    - Choose pivot (since elements are random, choose 1st element)
    - Find an element in the left side (using leftmark index starting at the
      beginning of the list just past the pivot that will move right) that is
      out-of-place (> pivot)
    - Find an element in the right side (using rightmark index starting at the
      end of the list moving left) that is out-of-place (< pivot)
    - Swap out-of-place elemetns with each other (swapping elements leftmark
      and rightmark refer to)
        - We're putting elements in the CORRECT side of the list
    - Continue doing this until rightmark index < leftmark index
        - In this case, swap the pivot element with the element rightmark refers to
        - We're putting the pivot element in the correct place!
'''

# partition function that will organize left sublist < pivot 
# and right sublist > pivot 
def partition(aList, first, last):
    pivotvalue = aList[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        # move leftmark until we find a left element > pivot
        while leftmark <= rightmark and aList[leftmark] <= pivotvalue:
            leftmark += 1

        # move rightmark until we find a right element < pivot
        while rightmark >= leftmark and aList[rightmark] >= pivotvalue:
            rightmark -= 1

        # check if we're done swapping left/right elements into CORRECT side
        if rightmark < leftmark:
            done = True
        else: # swap left and right elements into correct side of list
            temp = aList[leftmark]
            aList[leftmark] = aList[rightmark]
            aList[rightmark] = temp
            
    # put the pivot value into the correct place
    temp = aList[first]
    aList[first] = aList[rightmark]
    aList[rightmark] = temp

    return rightmark
            

# helper function so we can pass in the first/last index of lists
def quickSortHelper(aList, first, last):
    if first < last:
        # will define the index of the left/right sublists
        splitpoint = partition(aList, first, last)

        # recursively sort the left/right sublists
        quickSortHelper(aList, first, splitpoint - 1)
        quickSortHelper(aList, splitpoint+1, last)


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)



# pytest
def test_quickSort():
   numList1 = [9,8,7,6,5,4,3,2,1]
   numList2 = [1,2,3,4,5,6,7,8,9]
   numList3 = []
   numList4 = [1,9,2,8,3,7,4,6,5]
   numList5 = [5,4,6,3,7,2,8,1,9]
   quickSort(numList1)
   quickSort(numList2)
   quickSort(numList3)
   quickSort(numList4)
   quickSort(numList5)

   assert numList1 == [1,2,3,4,5,6,7,8,9]
   assert numList2 == [1,2,3,4,5,6,7,8,9]
   assert numList3 == []
   assert numList4 == [1,2,3,4,5,6,7,8,9]
   assert numList5 == [1,2,3,4,5,6,7,8,9]


'''
Quicksort Analysis
- Best-case running time is O(n log n)
    - In the best case, there are log n levels.
      Each level is O(n) when performing the partition step
- However, the worst case is O(n2)
    - Consider the case where the list is already sorted (or in reverse order)
    - The sub lists aren’t evenly divided for every recursive call
    - Quick Sort performance is dependent on the pivot value!
    - Can try to improve the pivot choice by selecting random values
      and choosing the medium
    - Textbook describes the median of three approach
        - Choose first, middle, and last element. Choose the median of these values
        - But even then, there is no guarantee that these values
          are good pivot values, but it does improve our chances that they are
- Note that Quicksort DOES NOT need extra space (unlike merge sort)
'''


'''
Trees Terminology
Node - An element in the tree. May have an incoming edge and many outgoing edges.
Edge - A connection between nodes (can be directional or bidirectional)
Root - The top most node (node without any incoming edges)
Path - The sequence of nodes from one node to a destination node along the tree
Children - Nodes that have incoming edges from another node
Parent - Contains outgoing edges to other child nodes
Sibling - Nodes that have the same parent
Subtree - A tree structure where the root of the tree is a child of a parent
Leaf - A node without any outgoing edges
Level - Number of edges from the root node to a destination node
Height - Maximum level of the entire tree
'''
