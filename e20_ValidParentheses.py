class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs of brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            if char in matching_bracket:
                # If the current character is a closing bracket
                # Check if the stack is not empty and top of the stack is the matching opening bracket
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()  # Pop the top element from the stack
                else:
                    return False  # If not matching, return False
            else:
                # If the current character is an opening bracket, push it to the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack


# Example usage:
sol = Solution()
print(sol.isValid("()"))  # Output: True
print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("(]"))  # Output: False
