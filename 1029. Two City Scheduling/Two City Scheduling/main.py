# -*- coding:utf-8 -*-

# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][
# 0], and the cost of flying the i-th person to city B is costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:
#
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
#
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

# Note:
#
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = [abs(c[0] - c[1]) for c in costs]
        new_costs = sorted(range(len(costs)), key=lambda x: diff[x])

        a_c = []
        b_c = []
        r = 0
        for i in new_costs:
            if costs[i][0] <= costs[i][1]:
                r += costs[i][0]
                a_c.append(i)
            else:
                r += costs[i][1]
                b_c.append(i)

        if len(a_c) > len(b_c):
            for i in b_c:
                new_costs.remove(i)
        elif len(a_c) < len(b_c):
            for i in a_c:
                new_costs.remove(i)

        return r + sum([diff[new_costs[i]] for i in range(abs(len(costs)/2-len(a_c)))])

        # N = len(costs)
        # diff = [c[0] - c[1] for c in costs]
        # indices = sorted(range(0, N), key=lambda k: diff[k])
        #
        # print diff
        # print indices
        #
        # result = 0
        # for i in range(int(N / 2)):
        #     result += costs[indices[i]][0]
        #     result += costs[indices[N - i - 1]][1]
        # return result


if __name__ == '__main__':
    costs = [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
    solution = Solution()
    r = solution.twoCitySchedCost(costs)

    print r
