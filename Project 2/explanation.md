## Problem 1 (Least Recently Used Cache)
Because the LRU Cache has `get` and `set` operation take `O(1)` time, my initial idea was using hash map data structure.
However, hash map does not have a mechanism of tracking which element has been used recently and which not. We can build
a double linked list on top of hash map values to keep track of the most recently used values (by moving the most recently
use value to the tail of the linked list). Luckily, in Python, there is already a data structure call **OrderedDict** that 
having those mechanism. So, I used **OrderdDict* to implement the LRU Cache

### Time complexity
The time complexity for both `get` and `set` operations are `O(1)`

### Space complexity
The space complexity is `O(n)`, with n is the capacity of the cache 

## Problem 2 (Finding Files)
Basically, the file system is organized as a tree. We can think of a regular file is a leaf node and a directory is an 
internal node (it can be a leaf node in case there is no regular file in the directory). So, the problem become performing
a tree search to find leaves that satisfy a condition (having a specific extension in this case). So, I perform a recursive
search to lookup for files and append the file name to an array when one is found.


### Time complexity
We traverse each node (file or directory) once. In each node, we do couple things such as call `os.path.isfile(..)` , or check 
 whether the path contain an extension (`p.endswith(..)`). If we assume those tasks have time complexity is O(1) then 
 the time complexity is `O(n)` where n is the number of files and directory

### Space complexity
I use an array to store the result. The space complexity is `O(m)` where m is the number of files will be found 

## Problem 3 (Huffman Coding)

My `HuffmanTree` consists of a tree `root`, `encode` table, `decode` table. When we initialize a `HuffmanTree` object, 
it does several steps:
1. Calculate the frequency table for the input data and store as a dictionary in format `{ char : freq }` (take `O(n)` time)
2. Convert the frequency table to an array of `HuffmanNode` in which each `HuffmanNode` contains a pair `{ char : freq }`
(take `O(m)` time)
3. Build a min-heap on top of the `HuffmanNode` array using heapq library (take `O(m*log(m))` time)
4. Build the tree by repeatedly merging two least frequency nodes until we have only one node in the array (take `O(m*log(m))` time)

### Time complexity
According to the steps above, the time complexity of building a HuffmanTree is `O(n*log(n))`    

### Space complexity
The space complexity is O(n)


## Problem 4 (Active Directory)
This problem is similar to Problem 2 - Finding files, where the group acts as a directory and user acts as a file. 
The difference is when we found the user, we stop searching and return. We will use recursion to perform the search in 
level order.
### Time complexity
In worst case, we traverse all the group and its sub-groups. So, The time complexity is O(n + m) in worst case, where 
n is number of the group and its sub-group and m is the number of user in the group.   

### Space complexity
The space complexity is O(1) because we only return True or False.

## Problem 5 (Block Chain)
The `BlockChain` class is implemented similarly to a singly linked list. The differences are instead of tracking of the 
head, we are tracking the tail, and when we add a new block, it will be added at the tail

 ### Time complexity
The time complexity is O(n)

### Space complexity
The space complexity is O(n)

## Problem 6 (Union and Intersection)
To implement the union and intersection problems, I use a hash map. The idea is that we traverse on two linked lists. 
In each element we traversed, if the element is not exist in the hash map, we put it into the map with the element as
 a key, and 0 as a value ( `{ node_value : 0 }`). If the element is already exist, as a key, in the hash map, we set
 its value = 1 (`{ node_value : 1 }`). Then:
In the union problem, all the keys in the hash map are the values we are looking for. So, just need to make a linked list
on top of those value  
In the intersection problem, all the keys that has value = 1 are the values we are looking for

 ### Time complexity
The time complexity for both `union(llist_1, llist_2)` and `intersection(llist_1, llist_2)`  are O(n + m) where 
`n = len(llist_1)` and  `m = len(llist_2)`

### Space complexity
In terms of space complexity, it depends on how many elements we have on the return linked list. In the worst case, 
both function will take `O(n + m)` space complexity. 