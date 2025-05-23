def roman_to_int(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    prev_value = 0

    for char in reversed(s):
        curr_value = roman_dict[char]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value

    return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.70 mb (Beats: 90.19%)
"""
