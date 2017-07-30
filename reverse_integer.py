class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sig = 0
        if x>0:
            sig = 1
        if x<0:
            sig = -1
        abs_x = abs(x)
        r = sig * int(str(abs_x)[::-1])
        if r>=2**31 or r<-2**31:
            return 0
        
        else:
            return r