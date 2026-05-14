class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1
        while k<len(nums):
            nums[k] = 0
            k+=1

#Essentially this is a two loop approach the first being a for loop that uses the variable k to get all non zero values to the first k positions
#The second loop is a while loop that then fills in the rest (len(nums) - k) with zeroes completeing the problem.
#Pretty simple problem, pretty simple solution