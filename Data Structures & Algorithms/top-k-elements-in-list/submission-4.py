from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        res = []
        
        for key, v in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            res.append(key)

        return res[:k]