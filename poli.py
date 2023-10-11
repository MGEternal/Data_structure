def is_palindrome_recursive(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    # Base case: If the string is empty or has only one character, it's a palindrome.
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same.
    if s[0] == s[-1]:
        # Recursively check the substring without the first and last characters.
        return is_palindrome_recursive(s[1:-1])
    else:
        return False
# Example usage:
input_string = "kmitl"
result = is_palindrome_recursive(input_string)
if result:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
