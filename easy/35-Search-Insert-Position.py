def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 18.64 mb (Beats: 25.91%)
"""
