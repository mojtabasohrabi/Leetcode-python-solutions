def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.98 mb (Beats: 20.21%)
"""
