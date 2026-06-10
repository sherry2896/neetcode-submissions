class Solution:
    def romanToInt(self, s: str) -> int:

        # Step 1: Define mapping of Roman symbols to integers
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        # Step 2: Traverse the string
        for i in range(len(s)):

            # Step 3: Check subtractive case
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total