# find the smallest number that n^2 <= number. n^2 >= n/2 where n > 1
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number * number == number:
        return number

    start = 0
    end = number
    found = False
    while start != end and start != end - 1:
        last_end = end
        end = (start + end) // 2
        if end * end == number:
            start = end
        elif end * end < number:
            start, end = end, last_end

    return start


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
