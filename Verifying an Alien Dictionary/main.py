# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        if not words:
            return True

        cost = {letter: i for i, letter in enumerate(order)}
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:  # compare only first unequal letters
                    if cost[first[j]] > cost[second[j]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False

        return True



class Solution(object):
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True


print(Solution().isAlienSorted(["word","world","row"]
,"worldabcefghijkmnpqstuvxyz"))

print(Solution().isAlienSorted(["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
