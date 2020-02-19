# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1

            for j, symbol in enumerate(needle):
                if i + j >= len(haystack) or symbol != haystack[i + j]:
                    break
            else:
                return i

        return -1
