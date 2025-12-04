import heapq

banks = []
with open("input.txt") as f:
    for bank in f:
        banks.append(bank.strip())

def findLargestVoltage(bank: str):
    right = len(bank) - 1

    maxAfterIndex = {}
    runningMax = int(bank[right])
    for i in range(len(bank) - 2, -1, -1):
        runningMax = max(runningMax, int(bank[i+1]))
        maxAfterIndex[i] = runningMax

    maxVoltage = 0
    for i in range(len(bank) - 1):
        maxVoltage = max(maxVoltage, int(bank[i] + str(maxAfterIndex[i])))
    print(maxVoltage)
    return maxVoltage

#Only heap results after the starting index are valid 
def pullFromHeapAfterIndex(h, index):
    res = heapq.heappop(h)
    while res[1] < index:
        res = heapq.heappop(h)
    return res

def findLargestVoltageByLength(bank: str, length: int):
    #Remove numbers one by one until we're left with numbers that MUST be in the solution
    # for i in range(1, 10):
    #     if len(bank) - bank.count(str(i)) > length:
    #         bank = bank.replace(str(i), "")
    #     else:
    #         break

    #Add to max heap sequentially so we know the K largest number before any given index 
    #By popping from the heap, we don't have to worry about duplicates
    h = []
    heapq.heapify(h)

    res = ""
    minIndex = -1

    for i in range(len(bank)):
        #Push current number to the heap, marking its index
        heapq.heappush(h, (-1 * int(bank[i]), i))

        #Once we reach the last N numbers in the bank, we can start assembling the answer
        if(i >= len(bank) - length):
            bestNumber = pullFromHeapAfterIndex(h, minIndex)
            res += str(-1 * bestNumber[0])
            minIndex = bestNumber[1]

    print(res)
    return int(res)

sum = 0
for bank in banks:
    sum += findLargestVoltageByLength(bank, 12)

print(sum)



