import random

print("Welcome to Number Guessing Game!")
print("Main 1 se 100 ke beech ek number soch raha hoon.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Apna guess daal: ")
    
    if not guess.isdigit():
        print("Bhai number daal, text nahi 🙏")
        continue
    
    guess = int(guess)
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Thoda bada soch!")
    elif guess > secret_number:
        print("Thoda chota soch!")
    else:
        print(f"Shabash! {attempts} attempt me jeet gaya 🔥")
        break