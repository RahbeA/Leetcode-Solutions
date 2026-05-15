class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_words = s.split(" ")
        newlist = [s for s in list_of_words if s]
        return len(newlist[-1])

#Simple solution that breaks string into list by whitespace, then removes white space via list comprehension, and then returns the length of the last word