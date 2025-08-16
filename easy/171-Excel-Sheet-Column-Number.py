def title_to_number(column_title: str) -> int:
    result = 0
    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.71 mb (Beats: 47.96%)
"""
