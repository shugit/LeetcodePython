class Solution:
    def intToRoman(self, num: int) -> str:
        h = {
            1:'I', 4:'IV',5:'V', 9:'IX',
            10:'X', 40:'XL',50:'L', 90:'XC',
            100:'C', 400:'CD',500:'D',900:'CM',
            1000:'M'
            }
        k = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        res = ""
        while num > 0:
            for n, letter in k:
                if n <= num:
                    num -= n
                    print(n, letter, num)
                    res += letter
                    break
        return res