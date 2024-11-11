message = "Hello World!"
print(message)

print(message.upper())
print(message.lower())


hobbies = ["Snowboarding", "MMA", "Ironman Race"]
print(hobbies)
for hobby in hobbies:
    print(hobby)
    
hobbies = ["Snowboarding", "MMA", "Ironman Race"]
hobbies.append("Basketball")
print(hobbies)
for hobby in hobbies:
    print(hobby)

hobbies = ["Snowboarding", "MMA", "Ironman Race", "Basketball"]
hobbies.pop()
print(hobbies) 
for hobby in hobbies:
    print(hobby)

hobbies = ["Snowboarding", "MMA", "Ironman Race"]
hobbies.sort()
print(hobbies)

hobbies.sort(reverse=True)
print(hobbies)
