class Solution:
    def romanToInt(self, s: str) -> int:
        # roman_to_int = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, 
        #                 "D" : 500, "M" : 1000}
        # num = 0
        # i = 0
        # while i < len(s):
        #     if i+1 < len(s) and c[i] == "I" and c[i+1] in [ "V", "X"]:
        #         num += roman_to_int[c[i+1]] - roman_to_int[c[i]]
        #         i += 1
        #     else:
        #         num += roman_to_int[c[i]]
        #     i += 1
        # return num
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
        