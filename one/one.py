import re

FILEINPUT = "./input.txt"
with open(file=FILEINPUT, mode="r") as file:
    aoc = file.readlines()

magicnumbers = 0
for line in aoc:
    numbers = re.findall(r'\d+', line)
    numbers = ''.join(numbers)
    magicnumbers += int(f"{numbers[0]}{numbers[-1]}")

print(magicnumbers)