def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.72 mb (Beats: 64.35%)
"""
