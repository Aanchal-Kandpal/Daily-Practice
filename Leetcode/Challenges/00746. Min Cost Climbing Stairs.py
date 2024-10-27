class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if cost == [] or len(cost) == 1:
            return 0

        min_cost_lst = [cost[0], cost[1]]
        n = 2
        while n < len(cost):
            min_cost_lst.append(min(min_cost_lst[n-1] + cost[n], min_cost_lst[n-2] + cost[n]))
            n += 1

        return min(min_cost_lst[-1], min_cost_lst[-2])
