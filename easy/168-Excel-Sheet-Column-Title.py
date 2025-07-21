def convert_to_title(column_number: int) -> str:
    result = []
    while column_number > 0:
        column_number -= 1
        remainder = column_number % 26
        result.append(chr(ord('A') + remainder))
        column_number //= 26
    return ''.join(result[::-1])


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.66 mb (Beats: 89.27%)
"""
