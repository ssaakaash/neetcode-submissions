class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need[c]: how many more copies of c window needs
        # formed = how many characters satisfies

        formed = 0
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        min_len = float('inf')
        min_win = [0, 0]

        left = 0
        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1

                if need[s[right]] >= 0:
                    formed += 1

            # print(min_win, left, right, formed)
            
            while left <= right and len(t) == formed:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_win[0] = left
                    min_win[1] = right

                if s[left] in need:
                    need[s[left]] += 1
                    
                    if need[s[left]] > 0:
                        formed -= 1

                left += 1

        return s[min_win[0]:min_win[1] + 1] if min_len != float('inf')  else ""