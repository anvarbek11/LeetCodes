class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        closeToOpen={")":"(","}":"{","]":"["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                     stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                     # loop through each character in the string

           