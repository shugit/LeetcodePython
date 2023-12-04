class TimeMap:

    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.h:
            self.h[key].append((timestamp,value))
        else:
            self.h[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h:
            return ""
        arr = self.h[key]
        left = 0
        right = len(arr)-1
        res = ""
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                right = mid - 1
            else:
                res = arr[mid][1]
                left = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)