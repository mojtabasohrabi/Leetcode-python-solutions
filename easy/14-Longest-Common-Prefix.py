def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.78 mb (Beats: 78.49%)
"""
