def binarySearch(input_list, lo , hi, number):


    while lo <= hi:
        mid = (lo + hi) // 2
        if input_list[mid] == number:
            return mid
        elif number < input_list[mid]:
            hi = mid - 1
        else:
            lo = lo + 1

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    lo = 0
    hi = len(input_list) - 1



    while lo <= hi:

        mid = (lo + hi) // 2
        if input_list[mid] == number:
            return mid

        if input_list[lo] <= input_list[mid]:                   # sorted array lies the left side
            if input_list[lo] <= number < input_list[mid]:
                return binarySearch(input_list, lo , mid, number)   # perform normal binary search on the left side
            else:
                lo = mid + 1
        else:                                                   # sorted array lies the right side
            if input_list[mid] < number <= input_list[hi]:
                return binarySearch(input_list, mid + 1, hi)
            else:
                hi = mid -1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def _test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
    _test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    _test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    _test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    _test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    _test_function([[6, 7, 8, 1, 2, 3, 4], 10])