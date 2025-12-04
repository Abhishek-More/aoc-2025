moves = []
with open("input.txt") as f:
    for move in f:
        moves.append(move.strip())


pos = 50
prevPos = 50
count = 0
for move in moves:
    dir = move[0]
    length = int(move[1:]) % 100
    if length == 0: continue

    print(count, pos, move)
    count += int(move[1:]) // 100

    
    if dir == "L":
        pos -= length
    elif dir == "R":
        pos += length

    if pos > 99:
        print("OVER", pos, move)
        pos -= 100
        count += 1
    elif pos < 0:
        print("UNDER", pos, move)
        pos += 100
        if not prevPos == 0:
            count += 1
    elif pos == 0:
        count += 1

    prevPos = pos

print(count)

