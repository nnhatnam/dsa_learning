## Problem 1 (Finding the Square Root of an Integer)
Call the given integer **n**. A way to look at this problem is finding an integer **k** in range **0, 1, 2, 3 ... n - 1 , n** such that
k is the biggest integer that k^2 <= n. So, what we need to do is perform a binary search within *range(n)* to find the index of **k**

### Time complexity
The time complexity is `O(log(n))`

### Space complexity
The space complexity is `O(1)` 

## Problem 2 (Search in a Rotated Sorted Array)
When a sorted array is rotated, there is always one half of the array still sorted and the other half is either a rotated sorted array
or a sorted array (when the rotation happens on half of the array such in case [3, 4, 1 , 2]) . If the number we are looking for in the sorted 
half, just perform a binary search. Otherwise, repeat the process on the other half 

### Time complexity
The time complexity is `O(log(n))`

### Space complexity
The space complexity is `O(1)` 

## Problem 3 (Rearrange Array Elements)
If we assume the array is sorted in descending order, a way to form two numbers that satisfies the given problem is form the first 
number by even index (O-based), and the second number by odd index. For example, [9, 8 , 7 , 6, 5] => 975 and 86. In this 
particular problem, sorting doesn't allowed, but we can use *heap* data structure to accomplish the same result. The idea is 
turn the array into a max-heap (or min-heap) then keep popping the root to form the two numbers until the array is empty. 

### Time complexity
Calling heapq.heapify cost O(n), and heapq.heappop cost O(log(n)). We call heappop n times (where n is the length of the array).
So, The time complexity is `O(n*log(n))`

### Space complexity
The space complexity is `O(1)` 

## Problem 4 (Dutch National Flag Problem)
After the array is sorted, we have three parts in the array: left part is 0, middle part is 1 and right part is 2. Say **i**  
is the partition between left and middle part (0 and 1), and **k** is the partition between middle and right part (1 and 2). An 
idea to resolve this problem is. 
1. Initialize **i** , **k** as a pointer to the beginning and the end of the input_list respectively
2. Have a pointer **j** traverses through the **input_list**. For each number in **input_list**, if the number < 1, we want 
it on the left part, so we move it before **i**. If the number = 0, we want it stay between **i** and **k**, so we do nothing.
If the number > 1, we want it on the right part, so we move it after **k**  

### Time complexity
It's single traverse, so the time complexity is `O(n)`

### Space complexity
The space complexity is `O(1)` since we only use three extra variables.

## Problem 5 (Building a Trie in Python)
This problem is about following definition and instructions to build a Trie. So, it's not many things to say about design choices
or algorithms.  
- TrieNode operation:  
    -  ``insert(self, char)`` : Add a child node represent the letter ``char`` to the node
    - ``suffixes(self, suffix = '')`` : Recursive function that collects the suffix for all complete words below this point
- Trie function:
    - `insert(self, word):`  : Add a word to the Trie
    - `find(self, prefix)` : Find the Trie node that represents this prefix

### Time complexity
- `TrieNode.insert` operation has time complexity is `O(1)` since insert a new key into dictionary cost `O(1)`
- `TrieNode.suffixes` operation is implemented using Depth-first search algorithms, so the time complexity is O(V + E) 
where V is the number of the vertices and E is the number of the edges. 
- `Trie.insert` operation has time complexity is `O(n)` where n is the length of the word
- `Trie.find` operation has time complexity is `O(n)` where n is the length of the word

### Space complexity
The space complexity of:
- `TrieNode.insert` is `O(1)`
- `TrieNode.suffixes` is `O(b*m)` where m is the length of the longest path and b is the number of the branches to travel
- `Trie.insert` is `O(n)`
- `Trie.find` is `O(1)`

## Problem 6 (Max and Min in a Unsorted Array)
Declare two variables for tracking the min and max of the array. Scan through the list, compare each number to the min and max 
 variables, and re-assign the min and max if needed 

### Time complexity
The space complexity is `O(n)` 

### Space complexity
The space complexity is `O(1)` 