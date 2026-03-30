class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # current maximum length string
        maxf = 0
        l = 0

        # to maintain count of letters
        count = {}

        #start from beginning
        for r in range(len(s)):
            #store the count of current letter in dict
            count[s[r]] = 1 + count.get(s[r],0)

            #check for the length of max string
            maxf = max(maxf, count[s[r]])

            #check if we have available number of swaps
            #if not increase l
            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
        return (r - l + 1)