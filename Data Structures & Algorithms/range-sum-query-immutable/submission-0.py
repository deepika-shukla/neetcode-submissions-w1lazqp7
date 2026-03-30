class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # claculate prefix sum
        self.prefix = [0] * len(nums)

        for i in range(len(self.nums)):
            if i <= 0:
                self.prefix[i] = self.nums[i]
            else:
                self.prefix[i] = self.prefix[i-1] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix[left - 1] if left > 0 else 0
        r = self.prefix[right]
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)