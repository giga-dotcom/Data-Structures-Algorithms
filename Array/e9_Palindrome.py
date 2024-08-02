def is_palindrome(x):
    # When x < 0, x is not a palindrome.
    # Also, if the last digit of the number is 0, in order to be a palindrome,
    # the first digit of the number also needs to be 0.
    # Only 0 satisfy this property.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    return x == reverted_number or x == reverted_number // 10


# Example usage:
x = 121
print(is_palindrome(x))  # Output: True

x = -121
print(is_palindrome(x))  # Output: False

x = 10
print(is_palindrome(x))  # Output: False