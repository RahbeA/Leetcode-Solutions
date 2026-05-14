#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
        return k

#Explanation: Essentially, this solution iterates through the array and uses the variable k in two ways simultaneously.
#First, it keeps count of integers in the array that dont equal the value "val" as defined in the functions parameter but also it's used as an index when setting the array's value to the current value being iterated in the for loop.
#This is because as specified in the probelm statment, the order may be changed so long as the first k values in the array are values not equal to k.
#In this way, the solution achieves the desired outcome without requiring additional space for a new array.
#I cooked.