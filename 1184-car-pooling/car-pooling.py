class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for n, f, t in trips:
            diff[f] += n
            diff[t] -= n
        print(diff[0:10])
        if diff[0] > capacity:
            return False
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
            if diff[i] > capacity:
                print(diff, capacity)
                return False
        return True