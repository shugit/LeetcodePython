class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        # candidates.sort(reverse=True)
        def bt(i, curSum):
            if curSum == target:
                res.append(subset[:])
                return
            if curSum > target:
                return
            for j in range(i, len(candidates)):
                subset.append(candidates[j])
                bt(j, curSum + candidates[j])
                subset.pop()
        bt(0, 0)
        return res