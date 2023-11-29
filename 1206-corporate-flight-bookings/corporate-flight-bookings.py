class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n+1)
        for start,end, num in bookings:
            arr[start-1] += num
            arr[end] -= num
        for i in range(1, n):
            arr[i] += arr[i-1]

        return arr[0:n]