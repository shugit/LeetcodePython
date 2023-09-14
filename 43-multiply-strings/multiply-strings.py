class Solution:
    def multiply(self, num1: str, num2: str) -> str:
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
                
                
