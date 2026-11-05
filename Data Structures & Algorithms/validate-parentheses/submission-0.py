class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bracket in s:
            if bracket in close_to_open:
                #closed bracket
                if not stack:
                    return False
                else:
                    op = stack.pop()
                    if close_to_open[bracket] != op:
                        return False
            else:
                #open bracket
                stack.append(bracket)

        if stack:
            return False
        else:
            return True
