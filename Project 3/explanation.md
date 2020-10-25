## Problem 1 (Finding the Square Root of an Integer)
Call the given integer **n**. A way to look at this problem is finding an integer **k** in range **0, 1, 2, 3 ... n - 1 , n** such that
k is the biggest integer that k^2 <= n. So, what we need to do is perform a binary search within *range(n)* to find the index of **k**

### Time complexity
The time complexity is `O(log(n))`

### Space complexity
The space complexity is `O(1)` 

