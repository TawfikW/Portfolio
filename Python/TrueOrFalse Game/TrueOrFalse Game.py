import random


def askQuestion():
    a = random. randint(1,100)
    b = random.randint(1,100)
    
    print ("a = " + str(a)+" b = "+ str(b))
    question = input("Is a bigger than b. y/n?: ")
    if question == 'y' and a>b or question == 'n' and a<b:
       print ("You are correct. GOOD job")
       playAgain()
       
    if question == 'n' and a>b:
        print ("You are wrong!")
        playAgain()

def playAgain():
    playAgain = input("Would you like to play again! y/n?")
    if playAgain == 'y':
        askQuestion()
    if playAgain == 'n':
        print ("Come back soon to play again!")

def start():
    print ("Helloo! This is a fun educational game.")
    name = input("What's your name: ")
    print (name +(", this is a game of True or False, to win you need to get 10 True!"))
    play = input ("Would you like to start! y/n?")
    if play == 'y':
        askQuestion()
    if play == 'n':
        print ("Come back soon to play again!")
    
start()


   
   
