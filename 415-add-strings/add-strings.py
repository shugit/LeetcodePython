class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = []
        carry = 0
        i, j = len(num1)-1, len(num2)-1
        while j >= 0:
            add = carry + int(num1[i]) + int(num2[j])
            res.append(str(add % 10))
            carry = add // 10
            i -= 1
            j -= 1
        while i >= 0 :
            add = carry + int(num1[i])
            res.append(str(add % 10))
            carry = add//10
            i -= 1
        if carry == 1:
            res.append(str(carry))
        res.reverse()
        return "".join(res)