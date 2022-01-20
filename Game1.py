import random, sys

print("Choose a number!");
print("Coded by Mwolf930 and a little help from Yaumama")

true = 0
false = 0

while True: # main game loop
        print("%s True, %s False.");
        while True:
            print("Enter your number or (q)uit.")
            playerMove = input()
            if playerMove == 'q':
                sys.exit()
             
            answer = random.randrange(0, 20)
            playerAnswer = input()
            if playerAnswer == answer:
                print("Correct!")
            else:
                print("Wrong, rip the correct answer was " + str(answer))