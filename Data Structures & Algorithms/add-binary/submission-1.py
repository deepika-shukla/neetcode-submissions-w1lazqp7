# class Solution:
#     def summ(self, a, b):
#         if a == "1" and b == "1":
#             return ["0", "1"]
#         elif a == "1" and b == "0":
#             return ["1","0"]
#         elif a =="0" and b =="1":
#             return ['1','0']
#         else:
#             return ['0','0']

#     def addBinary(self, a: str, b: str) -> str:
#         carry = "0"
#         i, j = len(a)-1, len(b)-1
#         binary_sum = ""

#         while i >= 0 or j >= 0 or carry == "1":
#             a1 = a[i] if i >=0 else '0'
#             b1 = b[j] if j >=0 else '0'
           
#             s, c = self.summ(a1, b1)
#             s, c2 = self.summ(s, carry)
#             carry, d = self.summ(c, c2)
#             binary_sum +=  s
#             i -= 1
#             j -= 1
        
#         return binary_sum[::-1]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = '0'
        res = []

        while i >= 0 or j >= 0 or carry == '1':
            x = a[i] if i >= 0 else '0'
            y = b[j] if j >= 0 else '0'

            # sum bit
            if x == y:
                res.append(carry)
                carry = x  # '1' only if both are '1'
            else:
                res.append('1' if carry == '0' else '0')
                # carry stays same

            i -= 1
            j -= 1

        return ''.join(reversed(res))
