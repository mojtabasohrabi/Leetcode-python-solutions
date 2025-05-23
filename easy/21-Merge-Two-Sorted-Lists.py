def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 or not l2:
        return l1 or l2

    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.68 mb (Beats: 88.81%)
"""
