class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}  # Dictionary to store the count of each character
        max_count = 0  # Variable to keep track of the maximum character count
        start = 0  # Start of the sliding window
        max_length = 0  # Maximum substring length with character replacement

        for end in range(len(s)):
            counts[s[end]] = counts.get(s[end], 0) + 1
            max_count = max(max_count, counts[s[end]])

            # If the number of characters to be replaced (k) is exceeded, shrink the window
            if (end - start + 1) - max_count > k:
                counts[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
        
