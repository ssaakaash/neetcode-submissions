class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in closing.keys():
                stack.append(c)
            elif len(stack) > 0:
                ele = stack.pop()
                if c != closing[ele]:
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True

        return False