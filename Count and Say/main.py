class Solution:
    def countAndSay(self, n: int) -> str:
        """
        11 -> 21 -> 1211 -> 111221 -> 312211 -> 13112221
        """

        if n == 1:
            return '1'
        if n == 2:
            return '11'

        result = ['1', '1']
        for _ in range(n - 2):

            count_equal_letters = 1
            term = []

            # trick for 1 extra iteration
            result.append('END')

            for j in range(len(result) - 1):

                if result[j + 1] != result[j]:
                    term.append(str(count_equal_letters))
                    term.append(result[j])
                    count_equal_letters = 1
                else:
                    count_equal_letters += 1

            result = term

        return ''.join(result)

