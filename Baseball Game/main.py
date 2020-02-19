# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: [str]) -> int:
        scores = []  # round scores
        result = 0
        for op in ops:
            if op == 'D':
                scores.append(scores[-1] * 2)
                result += scores[-1]
            elif op == '+':
                last_two = scores[-1] + scores[-2]
                scores.append(last_two)
                result += scores[-1]
            elif op == 'C':
                result -= scores.pop()
            else:
                scores.append(int(op))
                result += scores[-1]

        return result


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
