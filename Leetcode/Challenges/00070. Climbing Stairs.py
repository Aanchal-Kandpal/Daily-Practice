class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        step_1 = 1
        step_2 = 2


        for i in range(2, n):
            steps = step_1 + step_2
            step_1 = step_2
            step_2 = steps
            
        return steps
