alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from ceasarart import logo
def ceasar(start_text, shift_amount, direction):
    
        end_text = ""
        if direction == "decode":
            shift_amount = shift_amount * -1
        #Encode
        for char in start_text:
            if char in alphabet:
                position_letter_in_list = alphabet.index(char)
                new_position = position_letter_in_list + shift_amount
                #Getting the new letter from list through the new position
                new_letter = alphabet[new_position]
                end_text = end_text + new_letter
            else:
                end_text = end_text + char
            
        print(f"The {direction}d message is {end_text} \n")
        
        
        
    

want_restart = True
while want_restart:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    start_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    ceasar(start_text, shift_amount,direction)
    
    user_choice = input("Do You want to Want to caepher again ? Enter Yes to Continue & No to Stop \n").lower()
    if user_choice == "yes":
        want_restart = True
    else:
        want_restart = False
        print("Ceasar Cipher Stopped Successfully")
