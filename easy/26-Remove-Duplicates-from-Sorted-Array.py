def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 19.05 mb (Beats: 29.60%)
"""
