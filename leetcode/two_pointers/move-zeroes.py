class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cont = 0

        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                cont+=1

        nums += [0]*cont