# Given an array of intervals intervals where intervals[i] = [start i , end i ], return the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping

def non_overlapping_intervals(intervals):
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res

intervals = [[1,2],[2,3],[3,4],[1,3]]
print("Input:", intervals)
print("Expected:", 1)
print("Received:", non_overlapping_intervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print("Input:", intervals)
print("Expected:", 2)
print("Received:", non_overlapping_intervals(intervals))

intervals = [[1,2],[2,3]]
print("Input:", intervals)
print("Expected:", 0)
print("Received:", non_overlapping_intervals(intervals))
