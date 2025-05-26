def my_sqrt(x: int) -> int:
    if x < 4:
        return x if x < 2 else 1

    left, right = 2, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.74 mb (Beats: 51.11%)
"""
