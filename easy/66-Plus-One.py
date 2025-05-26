def plus_one(digits: List[int]) -> List[int]:
    return list(map(int, str(int(''.join(map(str, digits))) + 1)))


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.73 mb (Beats: 49.93%)
"""
