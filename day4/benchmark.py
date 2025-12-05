import time
import sys

def parse_input():
    """Parse the input file"""
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
    return intervals, items

def merge_intervals(intervals):
    """Merge overlapping intervals"""
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
    
    return mergedIntervals

def findInterval(intervals, item):
    """Binary search for item in intervals"""
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

def solve():
    """Main solution logic"""
    intervals, items = parse_input()
    mergedIntervals = merge_intervals(intervals)
    
    # Count items in intervals
    count = 0
    for item in items:
        if findInterval(mergedIntervals, int(item)):
            count += 1
    
    # Calculate total sum
    total_sum = 0
    for interval in mergedIntervals:
        total_sum += interval[1] - interval[0] + 1
    
    return count, total_sum, len(intervals), len(items), len(mergedIntervals)

def benchmark_solution():
    """Benchmark the solution"""
    start_time = time.perf_counter()
    count, total_sum, intervals_count, items_count, merged_count = solve()
    end_time = time.perf_counter()
    
    return {
        'time': end_time - start_time,
        'count': count,
        'sum': total_sum,
        'intervals_processed': intervals_count,
        'items_processed': items_count,
        'merged_intervals': merged_count
    }

def run_benchmark(num_runs=10):
    """Run benchmark multiple times and report statistics"""
    
    print(f"Running benchmark {num_runs} times...")
    print("=" * 50)
    
    times = []
    results = []
    
    for i in range(num_runs):
        result = benchmark_solution()
        times.append(result['time'])
        results.append(result)
        print(f"Run {i+1:2d}: {result['time']*1000:.2f}ms")
    
    # Calculate statistics
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    print("\n" + "=" * 50)
    print("BENCHMARK RESULTS")
    print("=" * 50)
    print(f"Average time: {avg_time*1000:.2f}ms")
    print(f"Min time:     {min_time*1000:.2f}ms")
    print(f"Max time:     {max_time*1000:.2f}ms")
    print(f"Runs:         {num_runs}")
    
    # Show solution results from last run
    last_result = results[-1]
    print(f"\nSolution Results:")
    print(f"Count:            {last_result['count']}")
    print(f"Sum:              {last_result['sum']}")
    print(f"Intervals read:   {last_result['intervals_processed']}")
    print(f"Items read:       {last_result['items_processed']}")
    print(f"Merged intervals: {last_result['merged_intervals']}")

if __name__ == "__main__":
    run_benchmark()