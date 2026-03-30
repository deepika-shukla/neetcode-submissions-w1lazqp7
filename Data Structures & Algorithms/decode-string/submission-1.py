class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        count = []
        j = 0
        while j < len(s):
            i = s[j]
            if i == ']':
                n = count.pop()
                a = stack.pop()
                cur = ''
                while stack and a != '[':
                    cur = a + cur
                    a = stack.pop()
                stack.append(cur*int(n))
            elif i.isdigit():
                c = ''
                while j < len(s) and s[j].isdigit():
                    c += s[j]
                    j+=1
                count.append(c)
                j-=1
            else:
                stack.append(i)
            j += 1
        
        final = ''
        while stack:
            final = stack.pop() + final
        return final