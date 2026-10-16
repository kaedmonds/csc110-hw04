# ------------------------------------------------------
#        Name: Kathryn Edmonds
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This chunk of code is trying to determine if the user inputs the word "dog" or "Dog", or uses the word "food" when prompted to input a sentence. """
    
    while True:
        given_st = input("give me a sentence: ") #asking for input
            
        if secret_word in given_st: #checking for secret word
            print("You used the secret word!")
            break
            
            if "dog" in given_st or "Dog" in given_st: #checking for dog
                print("You used the word \"dog\" or the word \"Dog\"!")
                break
        
        elif "dog" in given_st or "Dog" in given_st: #checking for word and dog
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        
        elif secret_word not in given_st or "dog" not in given_st or "Dog" not in given_st: #if sentence contains none of it
            print("Try again")


    
# Task 2
def check_greater():
    """ This chunk of code asks the user to input two integers, and then checks if the first is greater than the second, or vice versa. If they are equal to each other, it prompts the user to input new values. """
    
    while True:
        x = int(input("give me an integer: ")) #asking for input
        y = int(input("give me another integer: "))
    
        if x == y: #determining if they're equal
            print("Try again")
        elif x > y: #determining if first is greater
            print("First is Greater")
            break
        elif x < y: #determining if second is greater
            print("Second is Greater")
            break



# Task 3
def get_special_numbers():
    """ This chunk of code checks prints the numbers 1-40 if they are odd, a multiple of three, and not a multiple of five. """
    
    for num in range(1,41):
        if num%2 != 0 and num%3 == 0 and num%5 != 0:
            print(num)
    


# Task 4.a
def my_for_loop():
    """ This chunk of code asks for a string from the user. If it is less than 2 or greater than 5 letters, the loop stops. If it has a space, the loop stops. If it fits in the parameters, it will identify the vowels and the consonants in the given word. """
    while True:
        word = input("Give me a string: ") #asking for input
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} #defining the vowels
        
        if not (2<= len(word) <= 5) or " " in word: #checking if in range and no spaces
            print("bad word")
            return
        
        for let in word:
            if let in vowels: #printing vowels
                print(f"letter {let} is a vowel")
            else:
                print(f"letter {let} is a consonant") #printing consonants
        break

# Task 4.b
def my_while_loop():
    """ This chunk of code asks for the user to input a, b, or c. If the user picks a, the loop repeats. If they pick b, the loop stops and prints goodbye. If they pick c, the system exits. If they pick any other letter, they are prompted to pick again. """
    
    while True:
        letter = input("input a, b, or c: ") #asking for input
        if letter == "a": #assigning task if user picks a
            continue
        elif letter == "b": #assigning task if user picks b
            print("Goodbye")
            return
        elif letter == "c": #assigning task if user picks c
            exit()
        else: #assigning taks if user doesn't pick a, b, or c
            print("try again")
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
