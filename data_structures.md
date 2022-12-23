# 1. Lists

## accessing list 
  - lst[x:y]: returns x+1 to y 
  - if element is in list: if "apple" in thislist:
## inserting
  - adding elements: cars.append("Honda")
  - appending 2 lists: lst1.extend(lst2)
  - inser element at position: thislist.insert(2, "watermelon")
## removing
   - removing elements: cars.pop(1), cars.remove("Volvo")  
   - return final element: lst.pop()

## sorting
   - sort (ascending): arr.sort()
   - sort (descending): arr.sort(reversed=True)
  
## count 
   - count number of occurences of x in arr: lst.count(x)

## find
   - index of an element in arr: arr.index(x)
  
## reverse
   - reverse: lst.reverse()

## clear
  - clear: lst.clear()

## copy
  - mylist = thislist.copy()

## List comprehension
  - newlist = [x for x in fruits if x != "apple"]
  - newlist = [x for x in range(10)]
  - newlist = [x for x in range(10) if x < 5]
  - newlist = [x.upper() for x in fruits]
  - newlist = [x if x != "banana" else "orange" for x in fruits]
   
   
# 2. Tuple

## Ordered, Unchangable, allow duplicate values
- updating can be done by converting them to list: list(tpl1)
- unpacking tuple
  - (green, yellow, red) = fruits
  - (green, yellow, *red) = fruits
  - (green, *yellow, red) = fruits
- join: tuple3 = tuple1 + tuple2

# 3. Sets

## Set items are unchangeable, but you can remove items and add new items, no duplicates
- adding: thisset.add("orange")
- appending 2 sets: set1.update(set2), set1.union(set2)
- removing: thisset.remove("banana"), thisset.discard("banana"), thisset.pop(), thisset.clear()
- remove method raises error if item doesn't exist while discard doesn't

# 4. Dictionary
- dict.keys()
- dict.values()
- dict.items()
- if "key" in dict
- dict["new_key"] = value
- dict["key"] = new_value
- dict.pop("key")


# 5. Stack
We implement stack by using python in-built ds dequeue, we can also do it with lists, both have O(1) complexity for adding and deletion but in case of lists 
the time complexity is amortized 
Python’s lists are implemented as dynamic arrays internally, which means they occasionally need to 
resize the storage space for elements stored in them when elements are added or removed. 
The list over-allocates its backing storage so that not every push or pop requires resizing. 
As a result, you get an amortized O(1) time complexity for these operations. where as dequeue uses doubly linked list and hence they are very fast.

- initializing: s = deque()
- adding: s.append(x)
- deletion: s.pop()


# 6. Queue
We implement queue using dequeue python in-built data structure rather than list because list deletion takes O(n) as deleting element at starting 
index needs repositioning all other elements towards its right

- initializing: s = deque()
- adding: s.append(x)
- deletion: s.popleft()

# 7. Priority Queue
priority queue differs from normal queue when we pop out an item, it gives us the element with highest priority
when we choose to implement priority queue using lists, which might cost us O(nlogn) time complexity because each time we insert an element we need to sort based on priority
Hence list might not be a good idea
here we use heap (list based heap) which gives us O(log n) complexity for insertion and deletion 

*here's what is heap exactly?* ( min heap and max heap - heapq in python by default min)
Heap is a binary tree where parent node is always greater/smaller than child nodes.

- import heapq
- q = []
- heapq.heapify(q)
- heapq.heappush(q,(3,"item"))
- heapq.heappop(q)

# 8. Heap 
O(log n) - insertion and deletion
Heap is binary tree where parent element is always smaller/greater than it's children
- Insertion: 
  -  we insert at the leaft node and then heapify 
- Deletion:
  - we delete the root node, swap root as leaft node and heapify
- Implementation: https://github.com/shravaniparsi/coding/blob/main/heap.py

# 9. Linked List Data Structure
*Time:
- Search - 0(n)
- Insert - O(1)
- Delete - O(1)
*Space - O(n)

linked list implementation and sums: 
- https://github.com/shravaniparsi/coding/blob/main/linked_list.py 
- https://github.com/shravaniparsi/coding/blob/main/double_linked_list.py
- https://github.com/shravaniparsi/coding/blob/main/circular_linked_list.py

# 10. Trees

## Traversals
inorder, preorder and post order

# 11. Graphs
BFS, DFS

Time complexity of BFS and DFS is O(V + E), where V is the number of nodes and E is the number of edges.

The space complexity of the algorithm is O(V).

# Merge sort
O(log n)
Implementation: 
# Quick sort
O(n^2) - time complexity O(log n) - space complexity
# heap sort
O(nlog n) - time complexity O(1) - space complexity
# Binary search
O(log n) - time complexity O(1) - space complexity
ordered dict
collections

