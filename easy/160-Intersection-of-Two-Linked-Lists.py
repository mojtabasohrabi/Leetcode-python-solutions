def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a is not b:
        a = headB if a is None else a.next
        b = headA if b is None else b.next
    return a


"""
this solution was accepted and get this results:

Runtime: 78 ms (Beats: 87.28%)

Memory: 28.32 mb (Beats: 17.17%)
"""
