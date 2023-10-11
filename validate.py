def valid_parentheses(str):
    # Function to check if a given string has balanced parentheses.
    def is_balanced(string):
        stack = []
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False  # Unmatched closing parenthesis.
                stack.pop()
        return not stack  # True if the stack is empty.

    # Base case: If the string is empty or has balanced parentheses, it'str valid.
    if not str or is_balanced(str):
        return True

    # Find the index of the first closing parenthesis.
    close_index = str.find(")")

    if close_index == -1:
        return False  # Unmatched closing parenthesis.

    # Recursively check the string without the outermost parentheses.
    return valid_parentheses(str[:close_index] + str[close_index + 1:])

# Test cases
str1 = "()()(((())))"
str2 = "()"
str3 = "(()()(())())"
str4 = "((()()"

print(valid_parentheses(str1))  # Should return True
print(valid_parentheses(str2))  # Should return False
print(valid_parentheses(str3))  # Should return True
print(valid_parentheses(str4))  # Should return False
