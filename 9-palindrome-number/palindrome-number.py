class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        b=str(x)
        z=b[::-1]
        if b==z:
            return True
        else:
            return False