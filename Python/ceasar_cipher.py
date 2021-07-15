alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           

   ______  ________       _       ______   ________  _______        ______  _____  _______  ____  ____  ________  _______     
 .' ___  ||_   __  |     / \    .' ____ \ |_   __  ||_   __ \     .' ___  ||_   _||_   __ \|_   ||   _||_   __  ||_   __ \    
/ .'   \_|  | |_ \_|    / _ \   | (___ \_|  | |_ \_|  | |__) |   / .'   \_|  | |    | |__) | | |__| |    | |_ \_|  | |__) |   
| |         |  _| _    / ___ \   _.____`.   |  _| _   |  __ /    | |         | |    |  ___/  |  __  |    |  _| _   |  __ /    
\ `.___.'\ _| |__/ | _/ /   \ \_| \____) | _| |__/ | _| |  \ \_  \ `.___.'\ _| |_  _| |_    _| |  | |_  _| |__/ | _| |  \ \_  
 `.____ .'|________||____| |____|\______.'|________||____| |___|  `.____ .'|_____||_____|  |____||____||________||____| |___| 
                                                                                                                              
  """
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        new_letter=alphabet[new_position]
        plain_text+=new_letter
    print(f"The encoded text is {plain_text}")

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_amount=shift)
else:
    print("Enter valid direction")