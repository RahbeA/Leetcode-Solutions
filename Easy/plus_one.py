class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] = digits[len(digits)-1] + 1
            return digits
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9 and i == 0:
                digits[i]=0
                digits.insert(0, 1)
                return digits
            elif digits[i] == 9:
                digits[i] = 0
                if i!=0 and digits[i-1] != 9:
                    digits[i-1] += 1
                    return digits
                else:
                    pass

#This solution works by checking 4 cases.
#First is the case that the digit is not 9 and just needs to add 1 so it adds one and returns the list
#Second is the case where the digit is 9 and it's the last digit so it sets it to 0 and adds 1 to the front
#Third is the case where the digit is 9 and it's not the last digit so it sets it to 0 and carries the 1 over to the next digit
#Fourth is the case where all digits are 9 so it sets them all to 0 and adds 1 to the front
#This is my solution for the plus one leet code problem