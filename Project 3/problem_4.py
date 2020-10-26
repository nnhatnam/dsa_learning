def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pivot = 1
    i, j, k = 0, 0, len(input_list) - 1
    # print("Start ", input_list)
    while j <= k:
        if input_list[j] < pivot:
            if i != j:
                input_list[i], input_list[j] = input_list[j], input_list[i]  # swap i and j
                i += 1
            else:
                j += 1
        elif input_list[j] > pivot:
            input_list[j], input_list[k] = input_list[k], input_list[j]  # swap j and k
            k -= 1
        else:
            j += 1
    return input_list


def _test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    _test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    _test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    _test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    _test_function([0, 0 , 0])
    _test_function([1, 1, 2, 2, 1, 1, 1, 2 , 2 , 1])
    _test_function([])
    _test_function([0, 0, 2, 2, 0, 0, 0, 2, 2, 0])