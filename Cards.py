import random   

def ShuffleDeck(bananas):
    random.shuffle(bananas)

def Fish(GoFish):
    print("Got : ", GoFish[12], "and", GoFish[13])

def Sum1(Sum):
    return Sum[12] + Sum[13]

def Num():
    "1" == 1, "2" == 2, "3" == 3, "4" == 4, "5" == 5, "6" == 6, "7" == 7, "8" == 8, "9" == 9
    "10" == 10, "J" == 11, "Q" == 12, "K" == 13, "A" == 14


#Deck #1 (Não Mexer)
deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
computer_deck = deck.copy()

command = ""

while (command != "No"):

    print("--------------------------------------")  
    print("This is your and the computer's deck :", deck)
    print("Continue? (Yes/No)")
    command = input()

    if (command == "Yes"): 
        print("--------------------------------------")  
        print("Enter |Shuffle| to shuffle")
        command1 = input()

        if (command1 == "Shuffle"):
            #Shuffle #2 
            ShuffleDeck(deck)
            ShuffleDeck(computer_deck)
            print("Shuffling decks...")
            
            print("--------------------------------------")  

            #Tabuleiro #3
            print(deck)
            print(computer_deck)

            print("--------------------------------------") 
            
            #Fish #4
            print("You")
            Fish(deck) 
            print("Computer")
            Fish(computer_deck)
            
            print("--------------------------------------") 

            #Compare #5
            if Sum1(deck) > Sum1(computer_deck):
                print("You won")

            elif Sum1(deck) < Sum1(computer_deck):
                print("Computer won")

            elif Sum1(deck) == Sum1(computer_deck):
                print("You tied")


            deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

print("I have quit!")