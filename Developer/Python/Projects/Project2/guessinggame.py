import random
num = random.randint(1,500)
count=1
while(count!= 0):
    guess=int(input("Enter your Guess: "))
    while(guess != num):
        if(guess > num):
            count += 1
            print("Guess Lower!")
            break
        else:
            count += 1
            print("Guess Higher!")
            break
    else:
        print("Congratulations,You Guessed it Right!")
        print(f"You guessed it in {count} tries")
        count = 0 
        