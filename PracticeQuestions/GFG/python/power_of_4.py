# you may use python module's
# just return true/false or 1/0
import math


class Solution:
    def isPowerOfFour(self, n):
        # code here
        if n < 0:
            return False
        if n == 1:
            # 4^0 = 1
            return True

        # Change of base rule for logarithms
        result = math.log(n) / math.log(4)
        return result.is_integer()


# {
# Driver Code Starts
# Your code goes here

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        num = int(input())
        if Solution().isPowerOfFour(num):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends
