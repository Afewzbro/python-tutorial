import random

def guess(x):
    random_number= random.randint(1,x)
    guessed_number=0
    while guessed_number != random_number:
        guessed_number= int(input("Guess a number between 1 and {x}: "))
        if guessed_number < random_number:
            print("Sorry, guess again. Too low.")
        elif guessed_number > random_number:
            print("Sorry, guess again, Too high.")
    
    print(f"Yay, congrats, you have guessed the number {random_number} correctly.")

def computer_guess(x):
    low=1
    high = x
    feedback = ""
    while feedback != "c":
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess=low # COULD ALSO BE HIGH B/C LOW=HIHG
        feedback= input(f"is {guess} too high (H), too low (L), or correct (C)").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low=guess+1
        
    print(f"yay! the computer guessed your number, {guess}, correctly!")
computer_guess(10)
