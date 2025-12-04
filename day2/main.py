numRanges = []
with open("input.txt") as f:
    inp = f.read()
    numRanges = inp.strip().split(",")

def checkNum(num):
    strNum = str(num)
    if len(strNum) % 2 == 1:
        return True
    
    halfway = int(len(strNum) / 2)
    if strNum[0:halfway] == strNum[halfway:]:
        return False

    return True

def checkNum2(num):
    strNum = str(num)
    if len(strNum) <= 1:
        return True
    
    for factor in factors[len(strNum)]:
        if not checkNumForFactor(num, factor):
            return False
    return True


def checkNumForFactor(num, factor):
    strNum = str(num)
    if not len(strNum) % factor == 0:
        return True

    splits = [strNum[i:i+factor] for i in range(0, len(strNum), factor)]
    print(splits)
    if len(set(splits)) == 1:
        return False

    return True

#Find max end of range 
maxLen = 0
for numRange in numRanges:
    numRange = numRange.split("-")
    end = int(numRange[1])
    maxLen = max(end, maxLen)

factors = {}
for i in range(1, len(str(maxLen)) + 1):
    iFactors = []
    for j in range(1, i):
        if i % j == 0:
            iFactors.append(j)
    factors[i] = iFactors

print(factors)

#I would merge intervals here but i verified the input ranges are disjoint, so we don't even need memoization
totalSum = 0
for numRange in numRanges:
    numRange = numRange.split("-")
    start = int(numRange[0])
    end = int(numRange[1])
    for i in range(start, end + 1):
        ans = checkNum2(i)
        if not ans:
            print("ADDING", i)
            totalSum += i

print(totalSum)

