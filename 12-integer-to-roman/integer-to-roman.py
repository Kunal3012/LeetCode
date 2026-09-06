class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral symbols and their respective values
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_numeral = ''
        i = 0

        # Iterate through the values and build the Roman numeral string
        while num > 0:
            # Check if the current value is less than or equal to the remaining number
            while num >= values[i]:
                # Append the corresponding symbol to the Roman numeral string
                roman_numeral += symbols[i]
                # Subtract the value from the number
                num -= values[i]
            # Move to the next symbol/value pair
            i += 1

        return roman_numeral