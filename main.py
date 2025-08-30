# Get a random English word
# Put that letters of word into a list
#determin the length of the list
# Put "_" of the lenght of list into another list
# Print the list
# Get a letter from the user
# If the letter is in the list
# Put the letter into the list
# else ask the user to try again
#if list2 == list1 then print win

from collections import Counter
# from random_word import RandomWords
import random
import time

words = [
    "apple", "mango", "grape", "peach", "melon", "cherry", "banana", "lemon", 
    "kiwi", "plum", "pear", "berry", "guava", "lychee", "papaya", "coconut", 
    "pineapple", "apricot", "watermelon",
    
    "india", "china", "japan", "brazil", "russia", "canada", "france", 
    "germany", "italy", "spain", "england", "mexico", "australia", 
    "turkey", "egypt", "nepal", "thailand", "argentina", "southkorea", "america"
]



# Return a single random word

if __name__ == '__main__':
    word = random.choice(words)
    list1 = list(word)
    list2 = []
    letterGuessed = ''
    chances = len(word) + 2
    
    print("")
    print("Guess the Word ")
    print("You have", chances, "chances to guess the word")
    
    time.sleep(1)
    
    for i in range(0, len(word)):
        print("_ ", end=" ")
        list2.append("_")
    print("")
    time.sleep(1)
    try:
        while list1 != list2 and chances != 0:
                letter = input("Enter a letter: ")
                            # Validation of the guess
                if not letter.isalpha():
                    print('Enter only a LETTER')
                    continue
                elif letter == "admin":
                    print(word)
                    continue
                elif len(letter) > 1:
                    print('Enter only a SINGLE letter')
                    continue
                elif letter in letterGuessed:
                    print('You have already guessed that letter')
                    continue
                
                
                if letter in list1:
                    n = word.count(letter)
                    
                    for i, char in enumerate(list1):
                        if char == letter:
                            list2[i] = letter
                    letterGuessed += letter
                        
                    print(" ".join(list2))
                    time.sleep(1)
                    print("You have guessed the right letter!!")
                    print("Chances left: ", chances, "\n")
                    
                    
                else:
                    chances -= 1
                    print(" ".join(list2))
                    print("You have guessed the wrong letter")
                    print("Chances left: ", chances, "\n")
                    time.sleep(1)
        
        if chances == 0:
            print("You have lost the game")
        else:
            print("You have won the game")
            print("The word was", word)
    except Exception as e:
        print(e)
