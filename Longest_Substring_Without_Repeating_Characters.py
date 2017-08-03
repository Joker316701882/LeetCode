def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    d = {}
    start = 0
    max_length = 1
    for i in range(len(s)):
        if s[i] in d and d[s[i]]>=start:
            start = d[s[i]] + 1
        else:
            max_length = max(max_length,i - start +1)
        d[s[i]] = i
    return max_length


