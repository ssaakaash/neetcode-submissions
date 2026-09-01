class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        def dfs(t, n, k):
            if t == 0:
                res.append(n)
            elif t < 0:
                return

            for i in range(k, len(nums)):
                num = nums[i]
                dfs(t - num, n + [num], i)

        dfs(target, [], 0)
        return res