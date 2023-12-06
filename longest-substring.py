def length_of_longest_substring(s: str) -> int:
    max_sub_string = ''
    ans = 0
    for c in s:
        if c not in max_sub_string:
            max_sub_string += c
            ans = max(ans, len(max_sub_string))
        else:
            max_sub_string = c
    return ans
    

print(length_of_longest_substring('abcabcea'))