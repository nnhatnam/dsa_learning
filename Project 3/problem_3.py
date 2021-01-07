import heapq


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    l = len(input_list)
    lo, hi = 0, len(input_list) - 1

    # case [1] => [1, 0]
    if lo == hi:
        return [input_list[lo], 0]

    # case [8, 9] => [8, 9]
    if hi - lo == 1:
        return input_list

    mid = lo + (hi - lo) // 2
    left = merge_sort_desc(input_list, lo, mid)
    right = merge_sort_desc(input_list, mid + 1, hi)

    i, j = 0, 0



# n1, n2 = 0, 0
#     heapq.heapify(input_list)
#
#     unit = 1  # use unit because heapify is min heap
#     for i in range(l // 2):
#         n1 = n1 + heapq.heappop(input_list) * unit
#         n2 = n2 + heapq.heappop(input_list) * unit
#         unit = unit * 10
#
#     if l & 1 == 1:  # if len is odd
#         n1 = n1 + heapq.heappop(input_list) * unit
#     return [n1, n2]

def merge_sort_desc(arr, lo, hi):

    if lo == hi:
        return [arr[lo]]

    if hi - lo == 1:
        if arr[lo] > arr[hi]:
            return [arr[lo], arr[hi]]
        else:
            return [arr[hi], arr[lo]]

    mid = lo + (hi - lo) // 2
    left = merge_sort_desc(arr, lo, mid)
    right = merge_sort_desc(arr, mid + 1, hi)

    # merge step
    result = []
    i , j = 0 , 0
    while i < len(left) or j < len(right):
        if i == len(left):
            result.append(right[j])
            j += 1
        elif j == len(right):
            result.append(left[i])
            i += 1
        else:
            if i < len(left) and left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    return result


def merge(arr1, arr2):
    p1 = 0
    p2 = 0


def _test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    print(merge_sort_desc([4, 6, 2, 5, 9, 8], 0, 5))
    # Udacity test cases
    _test_function([[1, 2, 3, 4, 5], [542, 31]])
    _test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    # Test 1: array is empty
    _test_function([[], [0, 0]])

    # Test 2: array has 1 element
    _test_function([[1], [1, 0]])

    # Test 3: array has 2 element
    _test_function([[1, 2], [1, 2]])

    # Test 4: others
    _test_function([[9, 8, 7, 6, 5], [975, 86]])
    _test_function([[5, 6, 7, 9, 8], [975, 86]])
