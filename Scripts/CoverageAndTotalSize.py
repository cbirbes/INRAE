input = open("test2.txt")

puits = -1
already = True
size = 0
TotalSize = 0
nbReads = 0
TotalReads = 0
for line in input:
    TotalReads += 1
    oldPuits = puits
    puits = line.split(" ")[0]

    if puits == oldPuits and already:
        already = False
        size = int(line.split(" ")[1])
    elif puits != oldPuits:
        nbReads += 1
        TotalSize += size
        already = True
        size = int(line.split(" ")[1])

print(str(nbReads))
print(str(TotalReads))
print(str(TotalSize))
