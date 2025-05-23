def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue
    return not stack


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.73 mb (Beats: 80.85%)
"""
