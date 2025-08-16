def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.61 mb (Beats: 81.49%)
"""
