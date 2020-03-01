# https://leetcode.com/problems/day-of-the-week/
from calendar import weekday


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
        return days[weekday(year, month, day)]


print(Solution().dayOfTheWeek(day=15, month=8, year=1993))
