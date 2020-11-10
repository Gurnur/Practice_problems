"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
Input:
[[0,30],[5,10],[15,20]]
Output: false
"""
class Solution:
    def meeting_rooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        for interval in intervals[1:]:
            if interval[0] < intervals[0][1]:
                return False
        return True

obj = Solution()
meetings = [[7,10],[2,4]]
print(obj.meeting_rooms(meetings))
