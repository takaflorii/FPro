def alomola(s: str) -> bool:
    return s == s[::-1]

def palindrome_index(s: str) -> int:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if alomola(s[left + 1 : right + 1]):
                return left
            if alomola(s[left : right]):
                return right
            return -1

        left += 1
        right -= 1

    return -1
