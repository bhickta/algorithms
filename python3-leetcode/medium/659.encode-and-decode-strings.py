class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, ptr = [], 0
        while ptr < len(str):
            j = ptr
            while str[j] != "#":
                j += 1
            length = int(str[ptr:j])
            res.append(str[j + 1 : j + 1 + length])
            ptr = j + 1 + length
        return res


Input = ["lint", "code", "love", "you"]
output = Solution().encode(Input)
decode = Solution().decode(output)
print(Input, output, decode, Input == decode)