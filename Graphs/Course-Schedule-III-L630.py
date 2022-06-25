'''
We are uing DP approach on consider/notconsider on sorted course list based on it's lastdate.

TLE error we are getting even though memoisation is used because there are multiple possibilities as currentDay can have multiple values and key can't be similar for rest of the recursive DP executions. Hence TLE is coming.

Solution: Max-heap approach to solve this

Idea: Max-heap contains the duartion of courses possible so far. Root is basicallly course with max duration. If while iterating through sortedlist of courses, we came across course whose duration is less than max-duration of course in max-heap then we can add current course and remove earlier max-duration course from heap. 

Max-heap time complexity Q(logN) so 

TC: O(N*logN)
SC: O(N)
'''

import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sortedlist = courses.copy()
        sortedlist.sort(key= lambda x : x[1])
        
        heap = []
        time = 0
        
        for course in sortedlist:
            if time + course[0] <= course[1]:
                heapq.heappush(heap,-1*course[0])
                time += course[0]
            elif len(heap) !=0 and (-1*heap[0]) > course[0]:
                removed = heapq.heappop(heap)
                heapq.heappush(heap, -1*course[0])
                time += course[0] - (-1*removed)
        
        return len(heap)
        
        
    
        
        
