class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        i = 0
        while i < n // 2:
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
            i += 1
        nums[:k], nums[k:] = nums[:k][::-1], nums[k:][::-1]
