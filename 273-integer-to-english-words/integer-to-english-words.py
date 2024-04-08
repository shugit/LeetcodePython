class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        less_than_20 =  ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        thousands = ['', ' Thousand', ' Million', ' Billion']
        res = []
        def get(n):
            if n == 0:
                return ""
            if n < 20:
                return less_than_20[n]
            elif 20 <= n < 100:
                return tens[n // 10] + get(n % 10)
            elif n < 1000:
                return get(n // 100) + " Hundred" + get(n % 100)
            else:
                for i in range(3, 0, -1):
                    p = pow(1000, i)
                    if n >= p :
                        return get(n // p) + thousands[i] + get(n % p)
            return ''
        return get(num).lstrip()