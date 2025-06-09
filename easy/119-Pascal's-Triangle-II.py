class Solution:
    def get_row(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]

        prev_row = [1]

        for i in range(1, row_index + 1):
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            prev_row = current_row

        return current_row


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 16.92 mb (Beats: 100%)
"""
