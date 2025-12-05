import heapq
import time
from typing import List

def load_banks() -> List[str]:
    banks = []
    with open("input.txt") as f:
        for bank in f:
            banks.append(bank.strip())
    return banks

def pullFromHeapAfterIndex(h, index):
    res = heapq.heappop(h)
    while res[1] < index:
        res = heapq.heappop(h)
    return res

def findLargestVoltageByLength_with_optimization(bank: str, length: int):
    # WITH optimization: Remove numbers one by one until we're left with numbers that MUST be in the solution
    for i in range(1, 10):
        if len(bank) - bank.count(str(i)) > length:
            bank = bank.replace(str(i), "")
        else:
            break

    h = []
    heapq.heapify(h)
    res = ""
    minIndex = -1

    for i in range(len(bank)):
        heapq.heappush(h, (-1 * int(bank[i]), i))
        if(i >= len(bank) - length):
            bestNumber = pullFromHeapAfterIndex(h, minIndex)
            res += str(-1 * bestNumber[0])
            minIndex = bestNumber[1]

    return int(res)

def findLargestVoltageByLength_without_optimization(bank: str, length: int):
    # WITHOUT optimization: Skip the removal step (lines 32-36)
    h = []
    heapq.heapify(h)
    res = ""
    minIndex = -1

    for i in range(len(bank)):
        heapq.heappush(h, (-1 * int(bank[i]), i))
        if(i >= len(bank) - length):
            bestNumber = pullFromHeapAfterIndex(h, minIndex)
            res += str(-1 * bestNumber[0])
            minIndex = bestNumber[1]

    return int(res)

def benchmark_function(func, banks: List[str], length: int, iterations: int = 5):
    times = []
    
    for _ in range(iterations):
        start_time = time.perf_counter()
        total_sum = 0
        for bank in banks:
            total_sum += func(bank, length)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    return {
        'avg_time': avg_time,
        'min_time': min_time,
        'max_time': max_time,
        'all_times': times
    }

def main():
    print("Loading banks...")
    banks = load_banks()
    print(f"Loaded {len(banks)} banks")
    
    length = 12
    iterations = 5
    
    print(f"\nBenchmarking with {iterations} iterations...")
    print("=" * 60)
    
    # Benchmark with optimization
    print("Testing WITH optimization (original code)...")
    with_opt_results = benchmark_function(findLargestVoltageByLength_with_optimization, banks, length, iterations)
    
    # Benchmark without optimization
    print("Testing WITHOUT optimization...")
    without_opt_results = benchmark_function(findLargestVoltageByLength_without_optimization, banks, length, iterations)
    
    # Results
    print("\n" + "=" * 60)
    print("BENCHMARK RESULTS")
    print("=" * 60)
    
    print(f"\nWITH optimization (lines 32-36):")
    print(f"  Average time: {with_opt_results['avg_time']:.6f} seconds")
    print(f"  Min time:     {with_opt_results['min_time']:.6f} seconds")
    print(f"  Max time:     {with_opt_results['max_time']:.6f} seconds")
    
    print(f"\nWITHOUT optimization:")
    print(f"  Average time: {without_opt_results['avg_time']:.6f} seconds")
    print(f"  Min time:     {without_opt_results['min_time']:.6f} seconds")
    print(f"  Max time:     {without_opt_results['max_time']:.6f} seconds")
    
    # Performance comparison
    speedup = without_opt_results['avg_time'] / with_opt_results['avg_time']
    print(f"\nPerformance comparison:")
    print(f"  Speedup with optimization: {speedup:.2f}x")
    
    if speedup > 1:
        print(f"  The optimization makes the code {speedup:.2f}x faster")
    else:
        print(f"  The optimization makes the code {1/speedup:.2f}x slower")

if __name__ == "__main__":
    main()