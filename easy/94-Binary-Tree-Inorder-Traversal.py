def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                result.append(current.val)
                current = current.right

    return result


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.76 mb (Beats: 53.88%)
"""
