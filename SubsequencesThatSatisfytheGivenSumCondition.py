# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
def numSubseq(self, nums: List[int], target: int) -> int:
    nums.sort()
    res = 0
    right = len(nums) - 1
    for left, num in enumerate(nums):
        while nums[right] + num > target and left <= right:
            right -=1
        if left <= right:
            res += 2**(right - left)

    return res % (10**9 + 7)
