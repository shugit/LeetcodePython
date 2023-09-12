class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.add2(a,b)
        res = ""
        carry = 0
        if len(a) > len(b):
            rest = ["0"]*(len(a)-len(b))
            b = "".join(rest)+b
        else:
            rest = ["0"]*(len(b)-len(a))
            a = "".join(rest)+a
        n = len(a)
        for i in range(n-1,-1,-1):
            charA = int(a[i])
            charB = int(b[i])
            result = charA + charB + carry
            res = str(result%2) + res 
            carry = result // 2
        if carry > 0:
            res = str(carry) + res
        return res
    def add2(self, a, b):
        a,b = int(a,2), int(b,2)
        res = a+b
        print(res)
        return bin(res)[2:]