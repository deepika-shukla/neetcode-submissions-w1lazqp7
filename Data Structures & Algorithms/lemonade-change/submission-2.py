class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = 0

        five, ten, twenty =0,0,0 # 3,0,

        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                if five > 0:
                    five -= 1
                else:
                    return False
                ten += 1
            if i == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
                twenty += 1
        return True
            