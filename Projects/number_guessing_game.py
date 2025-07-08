import random
while(True):

    a=random.randint(1,100)
    max_attempt=7
    print("Number Guessing game\n Guess the number win the jackpot.")
    print("The attempts you have is 7")
    b=int(input("Enter your guess:"))
    count=0
    while(a!=b and count<max_attempt):
    
        count=count+1
        print(f"The left attempts you have now is{max_attempt-count}")
        if(a>b):
            print("Guess higher")
            b=int(input("Enter your guess:"))
        else:
            print("Guess Lower")
            b=int(input("Enter your guess:"))
        

    if(a==b):
        print("YOU WON JACKPOT")
        count=count+1
        print("the attempts:",count)
    else:
        print(f"The correct number is {a}\n GAME OVER")
    

    print("Do you want to play more ?")
    ans=input("Enter yes or no :")
    response= ans.lower()
    if(response =="yes"):
        continue
    else:
        print("Thanks for playing")
        break

