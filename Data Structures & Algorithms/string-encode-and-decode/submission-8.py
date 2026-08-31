class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i] != '#':
                length_str += s[i]
                i += 1

            length = int(length_str)
            word = s[i + 1: i + 1 + length]
            res.append(word)

            i += length + 1

        return res