def str_str(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.69 mb (Beats: 81.35%)
"""
