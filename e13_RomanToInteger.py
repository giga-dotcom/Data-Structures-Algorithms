def roman_to_int(s):
    # Mapping of Roman numerals to their integer values
    roman_to_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Initialize total to 0
    prev_value = 0  # Initialize previous value to 0

    # Iterate through the string in reverse
    for char in reversed(s):
        value = roman_to_value[char]  # Get the integer value of the current Roman numeral
        # If current value is less than previous value, subtract it from total
        if value < prev_value:
            total -= value
        else:
            # Otherwise, add it to total
            total += value
        prev_value = value  # Update previous value

    return total


# Example usage:
s1 = "III"
print(roman_to_int(s1))  # Output: 3

s2 = "LVIII"
print(roman_to_int(s2))  # Output: 58

s3 = "MCMXCIV"
print(roman_to_int(s3))  # Output: 1994
