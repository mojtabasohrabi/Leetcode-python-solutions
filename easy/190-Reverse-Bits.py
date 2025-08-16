def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


"""
this solution was accepted and get this results:

Runtime: 40 ms (Beats: 50.85%)

Memory: 17.93 mb (Beats: 9.54%)
"""
