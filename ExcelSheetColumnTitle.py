total = 26

def get_char(number, power):
    #Example :900000000 = b*26^6+c^26^5+d*26^4+e*26^3+f*26^2+g*26^1+h*26^0
    #Example :26 = 0*26^1+0*26^0 = Z => 26*26^0
    #Example :476 = 1*26^2+0*26^1+0*26^0 = ZZ
    #Example :477 = 1*26^2+0*26^1+1*26^0 = AAA
    #Example : 1355= 1*26^2+26*26^1+3*26^0 = AZC
    array = [None]*(power+1)
    reminder = number
    for i in reversed(range(power+1)):
        print 'i=%d,reminder=%d'%(i,reminder)
        #array[power-i] = to_char(reminder/pow(total,i))
        index = power-i
        value = reminder/pow(total,i)
        array[index] = value
        print 'array[%d]=%r'%(power-i,array[power-i])
        reminder = reminder%pow(total,i)
    array = down_fill(array)
    return array

def down_fill(array):
    zero_exist = False
    zero_index = None
    for key,value in enumerate(array):
        if value == 0:
            zero_exist = True
            zero_index = key
    if zero_exist:





def to_char(index):
    return chr(index - 1 + ord('A'))

def down_char(char):
    if char == 'A':
        return None
    return chr(ord(char)-1)
def to_str(array):
    str = ''
    for c in array:
        if c is not None:
            str+=c
    return str

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        if n == 0:
            return None
        elif n == 1:
            return 'A'
        i = 0
        for i in range(0,10000):
            if n <= pow(total,i):
                break
        #print i
        result = get_char(n, i-1)
        #return to_str(result)
        return result


s = Solution()
#print s.convertToTitle(1)
#print s.convertToTitle(2)
print s.convertToTitle(702)
#print s.convertToTitle(1355)
#26=Z
#27=AA
#52 = AZ = 1*26^1+1*26^0 but not 2*26^1+0*26^0
#675 = YY
#676 = YZ?
#print s.convertToTitle(26) # Z
#print s.convertToTitle(40) # Z
#print s.convertToTitle(52) # AZ
#print s.convertToTitle(676) # ZZ

#print s.convertToTitle(677) # ZZ
# print s.convertToTitle(677)
#print s.convertToTitle(27)
#print s.convertToTitle(30)
#print s.convertToTitle(90)
#print s.convertToTitle(900)
#print s.convertToTitle(900000000)

'''
AAAA
26*26*26*26 possibles

    1 -> A = 1*26^0
    2 -> B = 2*26^0
    26 -> Z = 26*26^0
    27 -> AA = 1*26^1+1
    28 -> AB = 1*26^1+2
    30 -> AD = 1*26^1+4
    90 -> CH = 3*26^1+12
    676 -> ZZ = 26*26^1 + 0
    677 -> AAA = 1*26^2 + 1
    900 -> =  AHP 1*26^2 + 8*26^1 + 16*26^0
    900000000 = a*26^7+b*26^6+c^26^5
'''
