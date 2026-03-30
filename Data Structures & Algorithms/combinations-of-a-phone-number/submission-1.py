class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_to_alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz", 
        }

        comb = []

        def backtrack(i, curS):
            if len(curS) == len(digits):
                comb.append(curS)
                return
            for c in nums_to_alpha[digits[i]]:
                backtrack(i+1, curS+c)
        
        if digits:
            backtrack(0, "")
        return comb