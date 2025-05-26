def length_of_last_word(s: str) -> int:
    lst = s.rstrip().split(" ")
    return len(lst.pop())


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.64 mb (Beats: 88.28%)
"""
