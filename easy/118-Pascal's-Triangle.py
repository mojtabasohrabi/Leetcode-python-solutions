class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0: return []
        t = [[1]]
        for i in range(1, num_rows):
            p = t[-1]
            n = [1] + [p[j] + p[j + 1] for j in range(len(p) - 1)] + [1]
            t.append(n)
        return t


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.74 mb (Beats: 58.34%)
"""
