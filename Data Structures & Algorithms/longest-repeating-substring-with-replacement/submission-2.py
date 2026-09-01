from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        start = 0

        max_len = 0
        max_freq = 0
        for end in range(len(s)):
            freq[s[end]] += 1
            if freq[s[end]] > max_freq:
                max_freq = freq[s[end]]

            while end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len