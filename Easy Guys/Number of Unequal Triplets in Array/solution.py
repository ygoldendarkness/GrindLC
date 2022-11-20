class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        result += 1
        return result
