class Solution:
    def has_cycle(self, head: ListNode) -> int:
        if not head or not head.next: return 0
        s, f = head, head
        while 1:
            s = s.next
            f = f.next
            if not f: return 0
            f = f.next
            if not f: return 0
            if s is f: return 1


"""
this solution was accepted and get this results:

Runtime: 44 ms (Beats: 80.36%)

Memory: 19.90 mb (Beats: 56.43%)
"""
