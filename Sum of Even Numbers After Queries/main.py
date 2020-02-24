# https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(self, a: [int], queries: [[int]]) -> [int]:
        even_sum = 0
        for num in a:
            if num % 2 == 0:
                even_sum += num

        result = []
        for value, i in queries:

            if a[i] % 2 == 0:  # a[i] was even
                if value % 2 == 0:  # a[i] will stay even
                    even_sum += value
                else:  # a[i] become odd
                    even_sum -= a[i]

                a[i] += value
            else:  # a[i] was odd
                if value % 2 == 0:  # a[i] will stay odd
                    a[i] += value
                else:  # a[i] become even
                    a[i] += value
                    even_sum += a[i]

            result.append(even_sum)

        return result


print(Solution().sumEvenAfterQueries([2, 0, 1, 1], [[1, 0], [1, 0], [-2, 0], [-2, 3], [-1, 3], [10, 3]]))
