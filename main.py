# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#task1
request = int(input("Type how many cups do u want: "))
total = request + request//6
print(f"Your total cups is {total}")

#task2
aX = int(input("aX = "))
aY = int(input("aY = "))
bX = int(input("bX = "))
bY = int(input("bY = "))
dist = (((bX-aX)**2)+((bY-aY)**2))**0.5
print(f"Distance is: {dist}")

#task3
cows = int(input("How many cows is on your farm? Type here: "))
pigs = int(input("How many pigs is on your farm? Type here: "))
chickens = int(input("How many chickens is on your farm? Type here: "))
legs = (cows+pigs)*4 + chickens*2
print(f"Total amount of legs is: {legs}")