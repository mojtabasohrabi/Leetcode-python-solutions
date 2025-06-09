class Solution:
    def max_profit(self, prices: List[int]) -> int:
        m, p = float('inf'), 0
        for x in prices:
            if x < m:
                m = x
            elif x - m > p:
                p = x - m
        return p


"""
this solution was accepted and get this results:

Runtime: 18 ms (Beats: 97.85%)

Memory: 26.93 mb (Beats: 33.02%)
"""
