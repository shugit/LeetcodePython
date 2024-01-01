class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def generate(num): 
            if intLength % 2 == 0:
                cur = int('1' + '0' * (intLength//2 - 1)) # k=4, cur = 10, k = 6, cur = 100
                cur +=  (num - 1)
                print(cur)
                if len(str(cur)) > intLength//2:
                    return -1
                return str(cur) + str(cur)[::-1]
            if intLength % 2 == 1:
                cur = int('1' + '0' * (intLength // 2))
                cur += (num - 1)
                if len(str(cur)) > intLength//2+1:
                    return -1
                return str(cur) + str(cur)[:-1][::-1]

        return [int(generate(x)) for x in queries]
            