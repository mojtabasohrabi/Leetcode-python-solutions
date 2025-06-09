class Solution:
    def single_number(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 19.55 mb (Beats: 77.62%)
"""
