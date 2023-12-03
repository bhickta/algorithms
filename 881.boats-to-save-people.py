#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        saves = 0
        people.sort()
        lptr, rptr = 0, len(people) - 1
        while(lptr <= rptr):
            if people[lptr] + people[rptr] <= limit:
                lptr += 1
                rptr -= 1
            else:
                rptr -=1
            saves += 1
        return saves
# @lc code=end
s=Solution()
s.numRescueBoats(people=[1, 6, 7, 8, 10], limit=10)
