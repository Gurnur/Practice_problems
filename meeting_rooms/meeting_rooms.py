"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
Input:
[[0,30],[5,10],[15,20]]
Output: false
"""
class Solution:
    def meeting_rooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

obj = Solution()
meetings = [[1,2],[2,4],[4,8],[3,8]]
print(obj.meeting_rooms(meetings))
