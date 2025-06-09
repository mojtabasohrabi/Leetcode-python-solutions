class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, result = [root], []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.70 mb (Beats: 83.19%)
"""
