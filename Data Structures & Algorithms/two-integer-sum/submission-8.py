from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(list)

        for i, num in enumerate(nums):
            index[num].append(i)

        for i, num in enumerate(nums):
            to_find = target - num
            for j in index[to_find]:
                if j != i:
                    return [i, j]

        return [-1, -1]