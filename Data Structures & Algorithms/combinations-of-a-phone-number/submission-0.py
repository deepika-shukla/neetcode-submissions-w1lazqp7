class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res  = []
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",      
        }

        def backtrack(i, curS):
            if len(curS) == len(digits):
                res.append(curS)
                return
            for c in dict[digits[i]]:
                backtrack(i+1,curS+c)

        if digits:
            backtrack(0, "")
        return res
