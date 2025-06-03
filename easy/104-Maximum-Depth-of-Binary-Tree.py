from collections import deque


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1

    return depth


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 19.10 mb (Beats: 29.66%)
"""
