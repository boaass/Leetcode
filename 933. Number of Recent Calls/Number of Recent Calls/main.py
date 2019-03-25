# -*- coding:utf-8 -*-

# Write a class RecentCounter to count recent requests.
#
# It has only one method: ping(int t), where t represents some time in milliseconds.
#
# Return the number of pings that have been made from 3000 milliseconds ago until now.
#
# Any ping with time in [t - 3000, t] will count, including the current ping.
#
# It is guaranteed that every call to ping uses a strictly larger value of t than before.

# Example 1:
#
# Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]

# Note:
#
#     1. Each test case will have at most 10000 calls to ping.
#     2. Each test case will call ping with strictly increasing values of t.
#     3. Each call to ping will have 1 <= t <= 10^9.


import collections

class RecentCounter(object):

    def __init__(self):
        self.ping_ts = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_ts.append(t)
        while self.ping_ts[0] < t-3000:
            self.ping_ts.popleft()

        return len(self.ping_ts)


if __name__ == '__main__':

    # Your RecentCounter object will be instantiated and called as such:
    # obj = RecentCounter()
    # param_1 = obj.ping(t)

    obj = RecentCounter()
    # param_1 = obj.ping()
    param_2 = obj.ping(1)
    param_3 = obj.ping(100)
    param_4 = obj.ping(3001)
    param_5 = obj.ping(3002)

    # print param_1
    print param_2
    print param_3
    print param_4
    print param_5