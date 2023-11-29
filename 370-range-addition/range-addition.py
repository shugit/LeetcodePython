class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length+1)
        for start,end,num in updates:
            arr[start] += num
            arr[end + 1] -= num
        for i in range(1, length):
            arr[i] += arr[i-1]
            
        return arr[0:length]