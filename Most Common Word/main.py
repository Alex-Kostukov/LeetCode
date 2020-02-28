# https://leetcode.com/problems/most-common-word/
from collections import defaultdict


class Solution:
    def mostCommonWord(self, text: str, banned: [str]) -> str:
        words = defaultdict(int)
        best = ('', 0)
        text = text + '|'
        i = -1
        while i < len(text) - 1:
            i += 1
            char = text[i]
            word = []
            while char.isalpha() and i < len(text) - 1:
                word.append(char.lower())
                i += 1
                char = text[i]

            cur = ''.join(word)
            if cur and cur not in banned:
                words[cur] += 1
                if words[cur] > best[1]:
                    best = (cur, words[cur])

        return best[0]
