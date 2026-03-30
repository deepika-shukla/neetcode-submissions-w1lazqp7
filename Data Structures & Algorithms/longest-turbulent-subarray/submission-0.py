class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # this question means, we have to find such a subarray
        # in which we get alternate sign, eg : 2,4,3,2,2,5,1,4
        # 2 <  5 > 1 < 4 : see alternate sign

        #but here we have a edge case if two numbers are equal
        # the we don't want to check for that number twice, we can move
        # one step forward

        l, r = 0, 1
        res, prev_sign = 1, ""

        # now traverse thourgh arr
        while r < len(arr):
            #check if current number is smaller or greater than previous number
            if arr[r-1] > arr[r] and prev_sign != ">": #making sure not alterante sign
                #update res
                res = max(res, r-l+1)
                r += 1
                #also update sign
                prev_sign = ">"
            elif arr[r-1] < arr[r] and prev_sign != "<":
                res = max(res, r-l+1)
                r += 1
                prev_sign = "<"
            else:
                #now if we found same sign
                # or = sign

                if arr[r] == arr[r-1]:
                    r = r + 1 # you can shift r to one step ahead
                # if not r will remain same

                #shift the left point
                l = r - 1

                #change the sign
                prev_sign = ""
        return res
