class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x:x[0])
        startTime.sort()
        memo = {}
        def dfs(i):
            if i >= len(startTime):
                return 0
            if i in memo:
                return memo[i]
            index = bisect_left(startTime, jobs[i][1])
            memo[i] = max(jobs[i][2] + dfs(index), dfs(i+1))
            return memo[i]
        return dfs(0)