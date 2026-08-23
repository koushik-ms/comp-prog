class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in match:
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
