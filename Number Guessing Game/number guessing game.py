print("Welcome,It's Guess The number game")
n=45
rem_guess=5
print("you have 5 chances to guess number")
print("Game starts NOW 3 2 1 GO...")
for i in range(5):
    a=int(input("enter the number:"))
    rem_guess=rem_guess-1
   
    if (a>100):
        print("Sorry,Your entered number is much greater")
        print("remaining chances:",rem_guess)
    elif(a<n and a>0):
        print("Sorry,Your entered number is little bit lesser")
        print("remaining chances:",rem_guess)
    elif(a>45 and a<60):
        print("You Atr about to reach that number")
        print("remaining chances:",rem_guess)
    elif(a>n):
        print("Sorry,Your entered number is liitle bit greater")
        print("remaining chances:",rem_guess)
    elif(a<0):
        print("Sorry,Your entered number is much lesser")
        print("remaining chances:",rem_guess)
    elif(a==0):
        print("Mtlb kuch bhi kya Lajwao mt ab yar Sorry,Your entered number is much lesser")
        print("remaining chances:",rem_guess)
        # break
    elif(a==n):
        print("YEY!!BOOOMMMMMMM,You entered the correct number,Congrats Party Paij bhawa")
   
print("Your have no chances left!,Play Again.")
        
