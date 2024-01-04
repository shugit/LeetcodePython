class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.sol2(num1, num2)

    def sol2(self, num1, num2):
        if num1 == "0" or num2 =="0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j]) + res[j+i+1]
                res[j+i+1] = mul % 10
                res[j+i] += mul // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return "".join(map(str, res[i:]))

    def sol1(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = [0] *(len(num1) + len(num2))
        for i in range(0, len(num1)):
            for j in range(0, len(num2)):
                carry_i = j + i
                mul = carry[carry_i] + int(num1[i]) * int(num2[j])
                carry[carry_i] = mul % 10
                carry[carry_i+1] = mul // 10 + carry[carry_i+1]
                # print(carry)
        carry.reverse()
        i = 0
        while carry[i] == 0:
            i += 1
        carry = carry[i:]
        # print(carry)
        carry = map(str, carry)
        return "".join(carry)
                
                
