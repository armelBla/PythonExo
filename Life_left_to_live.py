age = int(input("what is your current age?"))

years_max_life = 90

life_to_live = years_max_life - age

days = life_to_live * 365
weeks = life_to_live * 52
months = life_to_live * 12

print(f"you have {days} days, {weeks} weeks, and {months} months left.")
