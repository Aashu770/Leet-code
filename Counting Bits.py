class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x=[]
        for i in range(num+1): x.append(bin(i).count("1"))
        return x