"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Approach:
Put start time and end time into two arrays and get them sorted
Basically, it use a pointer to maintain minimum value of next end time as a simulation of poll() element in PriorityQueue
Beats over 100% submissions

Explanation:
https://www.jianshu.com/p/28475d91d54b?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
"""

class Solution:
    def meeting_rooms(self, intervals):
        start, end = [], []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])

        start.sort()
        end.sort()

        rooms, count = 0, 0
        for i in range(len(intervals)):
            if start[i] < end[count]:
                rooms += 1
            else:
                count += 1

        return rooms
obj = Solution()
meetings = [[0,30],[5,10],[15,20]]
print(obj.meeting_rooms(meetings))