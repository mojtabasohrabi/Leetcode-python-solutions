class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            a, b = s[l], s[r]
            if not (a.isalnum()):
                l += 1
                continue
            if not (b.isalnum()):
                r -= 1
                continue
            oa, ob = ord(a), ord(b)
            if (oa | 32) != (ob | 32):
                return False
            l += 1
            r -= 1
        return True


"""
this solution was accepted and get this results:

Runtime: 3 ms (Beats: 98.94%)

Memory: 17.94 mb (Beats: 83.25%)
"""
