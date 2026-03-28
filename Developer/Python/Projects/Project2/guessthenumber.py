import random
num = random.randint(1,100)
guess = -1
count=0
while(guess != num):
    count += 1
    guess=int(input("Enter your Guess: "))
    if(guess > num):
        print("Guess Lower!")
    elif(guess < num):
        print("Guess Higher!")

print(f"Congratulations! You guessed it right in {count} tries!")

