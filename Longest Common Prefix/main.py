# https://leetcode.com/problems/longest-common-prefix/

from collections import defaultdict


class Solution:
    def longestCommonPrefix(self, words: [str]) -> str:
        if not words:
            return ''

        prefixes = defaultdict(int)

        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                prefixes[prefix] += 1

        need_n = len(words)
        longest = ''
        for prefix, item in prefixes.items():
            if item == need_n and len(longest) < len(prefix):
                longest = prefix

        return longest
