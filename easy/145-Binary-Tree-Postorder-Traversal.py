class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack1, stack2 = [root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        result = []
        while stack2:
            result.append(stack2.pop().val)
        return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.52 mb (Beats: 97.56%)
"""
