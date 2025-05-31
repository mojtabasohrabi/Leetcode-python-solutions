def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1

    first, second = 1, 2
    if n == 1:
        return first
    if n == 2:
        return second

    for _ in range(3, n + 1):
        first, second = second, first + second
    return second


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 18.00 mb (Beats: 07.91%)
"""
