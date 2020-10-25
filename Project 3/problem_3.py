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
    n1, n2 = 0, 0
    heapq.heapify(input_list)

    unit = 1  # use unit because heapify is min heap 
    for i in range(l // 2):
        n1 = n1 + heapq.heappop(input_list) * unit
        n2 = n2 + heapq.heappop(input_list) * unit
        unit = unit * 10

    if l & 1 == 1:  # if len is odd
        n1 = n1 + heapq.heappop(input_list) * unit
    return [n1, n2]


def _test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
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
