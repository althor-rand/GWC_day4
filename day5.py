#DAY5 - write to file && for in range && while loop

# creates a "names.txt" file and writes on it
# or if the file already exists replaces the content of it
with open("names.txt", "w") as file:
    for i in range(3):
        name = input("Enter a name: ")
        file.write(name + "\n")
print("All names saved!")

print("=====") #section divider

# prints integers from 1 to 5
for x in range(1,6):
    print(x)

print("=====")#section divider

# prints integers from 0 to 8 increaments of 2
for x in range(0,10,2):
    print(x)

print("=====") #section divider    

# prints "Counting: 0"; "Counting: 1"; "Counting: 2"
count = 0
while count < 3:
    print("Counting:", count)
    count +=1

print("=====") #section divider    

# prints integers from 0 to 2, but skips 1 because of the if statement
for i in range(3):
    if i == 1:
        continue
    print(i)