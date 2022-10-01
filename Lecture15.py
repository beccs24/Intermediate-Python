# Lecture 15

'''
Priority Queues
- In a Queue structure, we can insert items to the back of the queue and
  remove items at the front of the queue
    - The order of elements in the queue were dictated by WHEN items were
      inserted into the queue
- Priority Queues are similar to Queues EXCEPT
    - We can insert items into the priority queue where an item has some value
      representing a priority, and items are ordered in the priority queue with
      respect to their priority value
'''

'''
Tree Properties
    - A BINARY tree is a tree where any node may have AT MOST two children
    - A BALANCED BINARY tree is when the left and right subtrees of every node differ
      in height by no more than 1
    - A COMPLETE tree is when every level of the tree, except the deepest, must
      contain as many nodes as possible. The deepest level must have all nodes
      to the LEFT as possible.
'''

'''
Heaps
- A heap is a COMPLETE binary tree

- MAXHEAP: A complete tree where the value (priority) of a node is never less
           than the value of its children
- MINHEAP: A complete tree where the value (priority) of a node is never greater
           than the value of its children


- Heaps are an efficient way to implement a Priority Queue
    - The only element we care about when removing from the priority queue is the
      root of the heap (the min value for a minHeap and the max value for a maxHeap)
      
- Since binary heaps have the complete tree property, representing this with a
  Python List is simple
    - Easiest to represent the heap in a Python list where the 0th element in
      the list is meaningless
    - The root of a binary heap is at index 1

- A node's index with respect to its parents and children can be generalized as:
    - A node's parent index: node_index // 2
    - A node's left child index: 2 * node_index
    - A node's right child index: 2 * node_index + 1
'''

'''
Insertion into Binary MaxHeap
- Insert the element in the first available location (note, will be at the end
  of the list)
- While the element's parent is less than the element we just inserted,
    - Swap the element with its parent

Insertion into Binary MinHeap
- Same algorithm as MaxHeap except we swap while the element's parent is
  GREATER than the element

- Insertion is O(log n) (height of tree is log n)
'''

'''
Removing Max (root) element from Binary MaxHeap
- Since heaps are used to implement priority queues, removing the root element is
  a commonly used operation
  
- Copy the root element into a variable
- Assign the last_elelment in the Python list to the root position (new_root)
- While new_root is less than one of its children,
    - Swap the largest child with the new_root
- Return the original root element

Removing Min (root) element from Binary MinHeap
- Same algorithm as MaxHeap except we swap the smallest child with the new_root

- Deletion is O(log n) (height of tree is log n)
'''

'''
# MinHeap
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) # return index of minimum child
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return val

# pytest
def test_BinHeap():
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    assert bh.delMin() == 3
    assert bh.delMin() == 5
    assert bh.delMin() == 7
    assert bh.delMin() == 11


bh = BinHeap()
bh.insert(40)
bh.insert(20)
bh.insert(30)
bh.insert(50)
bh.insert(10)
print(bh.heapList)
'''

class max_heap: 
    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.Heap = [0]*(self.sizelimit + 1)
        self.Heap[0] = sys.maxsize
        self.root = 1
 
 
    # helper function to swap the two given nodes of the heap
    # this function will be needed for max-heapify and insertion 
    # in order to swap nodes which are not in order (not satisfy max-heap property)
    def swapnodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]
  
    # THE MAX_HEAPIFY FUNCTION
    def max_heapify(self, i):
  
        # If the node is a not a leaf node and is lesser than any of its child
        if not (i >= (self.cur_size//2) and i <= self.cur_size):
            if (self.Heap[i] < self.Heap[2 * i]  or  self.Heap[i] < self.Heap[(2 * i) + 1]): 
                if self.Heap[2 * i] > self.Heap[(2 * i) + 1]:
     # Swap the node with the left child and call the max_heapify function on it
                    self.swapnodes(i, 2 * i)
                    self.max_heapify(2 * i)
  
                else:
                # Swap the node with right child and then call the max_heapify function on it
                    self.swapnodes(i, (2 * i) + 1)
                    self.max_heapify((2 * i) + 1)
  
 
 
    # THE HEAPPUSH FUNCTION
    def heappush(self, element):
        if self.cur_size >= self.sizelimit :
            return
        self.cur_size+= 1
        self.Heap[self.cur_size] = element 
        current = self.cur_size
        while self.Heap[current] > self.Heap[current//2]:
            self.swapnodes(current, current//2)
            current = current//2
  
  
    # THE HEAPPOP FUNCTION
    def heappop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.max_heapify(self.root)
        return last
  
  
    # THE BUILD_HEAP FUNCTION
    def build_heap(self): 
        for i in range(self.cur_size//2, 0, -1):
            self.max_heapify(i)
  
  
    # helper function to print the heap
    def print_heap(self):
        for i in range(1, (self.cur_size//2)+1):
            print("Parent Node is "+ str(self.Heap[i])+" Left Child is "+ str(self.Heap[2 * i]) +                  " Right Child is "+ str(self.Heap[2 * i + 1]))
  
  
 
maxHeap = max_heap(10)
maxHeap.heappush(15)
maxHeap.heappush(7)
maxHeap.heappush(9)
maxHeap.heappush(4)
maxHeap.heappush(13)
maxHeap.print_heap()
