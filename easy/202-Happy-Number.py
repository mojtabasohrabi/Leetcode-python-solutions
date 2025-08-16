def is_happy(n: int) -> bool:
    def get_next(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1


"""
this solution was accepted and get this results:

Runtime: 0 ms (Beats: 100%)

Memory: 17.99 mb (Beats: 18.25%)
"""
