row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_digit = int(position[0]) - 1
last_digit = int(position[-1]) - 1

map[last_digit][first_digit] ='x'

print(f"{row1}\n{row2}\n{row3}")