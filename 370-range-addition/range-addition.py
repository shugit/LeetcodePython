class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length+1)
        for start,end,num in updates:
            arr[start] += num
            arr[end + 1] -= num
        prefix = arr[0]
        for i in range(1, length):
            arr[i] += prefix
            prefix = arr[i]
            
        return arr[0:length]