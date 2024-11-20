import random
start = int(input("Enter the start of the number: "))
end = int(input("Enter the end of the number: "))
k = random.randint(start,end)
print("The computer will think of a number between ",start, "and ", end)
guess = int(input("Enter your guess here: "))
try1 = 1 
while try1 <= 3:
    if guess == k:
        print("Congragulation you have won the game")
        break
    elif guess < k:
        print("Too Low")
    elif guess > k:
        print("Too High")
    try1 += 1 
    if try1 < 4:
        guess = int(input("TRY AGAIN: "))
if try1 == 4:
    print("Sorry you have finished your chances")