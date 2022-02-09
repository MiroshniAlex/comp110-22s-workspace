"""Lists Game Example."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 12))

print(rolls)

rolls.pop()
print(rolls)

i = 0
sum = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(sum)
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# print(rolls[0])