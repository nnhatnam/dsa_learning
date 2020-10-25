# find the smallest number that n^2 <= number. n^2 >= n/2 where n > 1
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number is None or number < 0:
        return None

    if number * number == number or number == 1:
        return number

    lo = 0
    hi = number
    while lo < hi:
        mid = (lo + hi) >> 1
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

if __name__ == "__main__":
    # Udacity test cases
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")

    # Test 1: number is None
    print("Pass" if (sqrt(None) is None) else "Fail")

    # Test 2: number negative
    print("Pass" if (sqrt(-1) is None) else "Fail")

    # Test 3: extra test cases
    print("Pass" if (10 == sqrt(100)) else "Fail")
    print("Pass" if (10 == sqrt(110)) else "Fail")
    print("Pass" if (10 == sqrt(120)) else "Fail")
    print("Pass" if (12 == sqrt(144)) else "Fail")

