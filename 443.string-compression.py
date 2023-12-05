#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        index = 0

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[index] = chars[i - 1]
                index += 1
                if count > 1:
                    for digit in str(count):
                        chars[index] = digit
                        index += 1
                count = 1

        return index

# @lc code=end

Solution().compress(["a","a","b","b","c","c","c"])