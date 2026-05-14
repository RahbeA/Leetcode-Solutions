class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        for i in range(len(nums)+1):
            if i not in nums:
                return i

#Simple solution for finding missing number via index since value starts from 0 and goes to n
#I use the index to check if a number is missing from 0 to n and then just return the index since it equals the value