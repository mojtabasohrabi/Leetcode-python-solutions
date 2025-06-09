class Solution:
    def min_depth(self, root):
        if not root: return 0
        q = [(root, 1)]
        while q:
            n, d = q.pop(0)
            if not n.left and not n.right: return d
            if n.left: q.append((n.left, d + 1))
            if n.right: q.append((n.right, d + 1))


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 50.31 mb (Beats: 47.12%)
"""
