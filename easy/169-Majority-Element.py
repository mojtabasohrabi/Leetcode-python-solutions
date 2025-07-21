def majority_element(nums: List[int]) -> int:
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


"""
this solution was accepted and get this results:

Runtime: 3 ms (Beats: 82.58%)

Memory: 19.28 mb (Beats: 86.73%)
"""
