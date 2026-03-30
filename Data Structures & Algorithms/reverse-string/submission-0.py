class Solution:
    def reverseString(self, s: List[str]) -> None:
        """9\
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()

        for i in range(0, len(s)//2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        
        