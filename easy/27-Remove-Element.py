def remove_element(self, nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.88 mb (Beats: 33.41%)
"""
