class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        str_rev = s[::-1]
        

        # for num in str_rep:
        #     s += num
        if str_rev == s:
            return True
        else:
            return False
