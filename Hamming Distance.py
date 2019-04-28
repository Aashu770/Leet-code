class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = '{0:032b}'.format(x)    #Convert x int to binary and format it with 45 padded 0 so their length is equal
        b = '{0:032b}'.format(y)
        count =0
        for i in range(len(a)):
            if a[i] != b[i]:
                count +=1
        return count