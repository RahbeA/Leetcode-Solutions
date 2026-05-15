class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
#Super easy solution that adds the integer casted values of the binary strings, then converts the sum back to a binary string
#Note: the "[2:]" is used to remove the 0b prefix from the string to return a clean binary value