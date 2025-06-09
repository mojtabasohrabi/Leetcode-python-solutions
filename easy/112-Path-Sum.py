class Solution:
    def has_path_sum(self, root, target_sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return target_sum == root.val
        return self.has_path_sum(root.left, target_sum - root.val) or self.has_path_sum(root.right,
                                                                                        target_sum - root.val)


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 19.14 mb (Beats: 24.05%)
"""
