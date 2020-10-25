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

