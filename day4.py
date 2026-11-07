season = input("what's your fav season?")
drink = input("what's your fav drink during that season?")
print("Your vibe is a ", drink, "during", season)

print("=====") #section divider

rain = input("is it raining? Enter 1 for Yes, or 2 for No: ")
temp = input("what is the temperature: ")

if rain == "1" and temp < "50":
    print("get an umbrella and wear a winter jacket")
elif rain == "1":
    print("get an umbrella and maybe a light jacket")
else:
    print("you dont need an umbrella")

print("=====") #section divider


pet = {
    "name": "Buddy",
    "animal" : "dog",
}

print("--- Original Dictionary ---")
print(pet)

pet["age"] = 3   # add a new key and value
print("\n---Updated Dictionary---")
print(pet)