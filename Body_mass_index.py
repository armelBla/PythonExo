height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

body_mass_index = int(weight / height ** 2)

print(f"Your BMI is {body_mass_index}")