def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.83 mb (Beats: 51.46%)
"""
