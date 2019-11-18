name = "Rogue"
age = "190"
gender = "M"
race = "mix_race : 20% high elf, 10% dragon_born, 10& dark elf, 30% human, 10% druid, 10% transmutter, 10% unknown"
clan = "warrior_warlock"
position = "Leader_candidate"
print(name)
print(age)
print(gender)
print(race.capitalize()) # .capitalize() makes 1st letter capital
print(clan)
print(position)
test = position.lower()
mm = test[0]
print(mm)

x = race.count("%")
print(x)
z = "i like programming"
new_var = z[0] # prints the first letter = starts from "0" last letter can be rep as "-1"
new_var = z[9:] # prints everything from starting point #
new_var = z[9:17] # prints from starting point to the value before the end point
new_var = z[9:18] # by increasing the value of the end point it prints everything from 9-17
print(new_var) # ps. python prints the last value of the words in bracket



