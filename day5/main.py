intervals = []
items = []
with open("input.txt") as f:
    itemsStarted = False
    for line in f:
        if itemsStarted:
            items.append(line.strip())
        else:
            if line == "\n":
                itemsStarted = True
                continue
            intervals.append(line.strip())

intervals = sorted(intervals, key=lambda x: int(x.split("-")[0]))
mergedIntervals = []

currStart = 0
currEnd = 0
for interval in intervals:
    start = int(interval.split("-")[0])
    end = int(interval.split("-")[1])
    if end > currEnd and start > currEnd:
        mergedIntervals.append([start,end])
        currStart = start
        currEnd = end
    elif end > currEnd and start <= currEnd:
        mergedIntervals[-1][1] = end
        currEnd = end

def findInterval(intervals, item):
    left = 0
    right = len(intervals)
    while left < right:
        mid = (left + right) // 2
        if intervals[mid][0] <= item <= intervals[mid][1]:
            return True
        elif item < intervals[mid][0]:
            right = mid
        else:
            left = mid + 1

    return False

count = 0
for item in items:
    if findInterval(mergedIntervals, int(item)):
        count += 1

print(count)

sum = 0
for interval in mergedIntervals:
    sum += interval[1] - interval[0] + 1

print(sum)
        
