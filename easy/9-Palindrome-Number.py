def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    string = str(x)
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True


"""
this solution was accepted and get this results:

Runtime: 3 ms (Beats: 88.33%)

Memory: 16.57 mb (Beats: 100%)
"""
