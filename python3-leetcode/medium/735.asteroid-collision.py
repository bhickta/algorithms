#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = asteroid + stack[-1]
                if diff == 0:
                    asteroid = 0
                    stack.pop()
                elif diff < 0:
                    stack.pop()
                else:
                    asteroid = 0
            if asteroid and asteroid != 0:
                stack.append(asteroid)
        return stack
# @lc code=end

Solution().asteroidCollision([-1, -2, 4, -5, 8])
