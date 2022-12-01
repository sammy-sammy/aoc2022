file = open("aocinput.txt")
calories = []
sum = 0
for line in file:
    calories.append(line.strip("\n"))

elves = []
sum = 0
for x in calories:
    if x != "":
        sum += int(x)
    else:
        elves.append(sum)
        sum = 0
print(sorted(elves))

total = 0
i = 0
while i < 3:
   total += sorted(elves)[len(elves)-i-1]
   i+=1

print(total)
