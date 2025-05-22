def two_sum(nums: List[int], target: int) -> List[int]:
    dictionary = {}
    for i in nums:
        value_to_find = target - i
        if value_to_find in dictionary.keys():
            return [nums.index(value_to_find), nums.index(dictionary[value_to_find], nums.index(value_to_find) + 1)]
        dictionary[i] = value_to_find
    return []


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.89 mb (Beats: 99.95%)
"""
