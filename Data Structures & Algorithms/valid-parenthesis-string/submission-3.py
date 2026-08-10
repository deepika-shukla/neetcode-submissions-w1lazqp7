class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax, leftmin = 0,0 # keeping track of open bracket
        # and the reason of two counts is * could be either closing or opening

        for c in s:
            if c == "(":
                leftmax, leftmin = leftmax+1, leftmin+1
            elif c == ")":
                leftmax, leftmin = leftmax-1, leftmin-1
            else:
                # considering for leftmin:  closing
                # for leftmax : open bracket
                leftmax, leftmin = leftmax+1, leftmin-1
            if leftmax < 0:
                return False
            if leftmin < 0:
                # reset
                leftmin =0
        return leftmin == 0