''' caesar cipher --- encryption and decrption technique '''
import string
def encrypt(message,shift):
    cipher_text=""
    for m in message:
        if m in letter:
            position=letter.index(m)
            # print(position)
            new_position=(position+shift)%26
            # print(new_position)
            cipher_text+=letter[new_position]
        else:
            cipher_text+=m
    print(f" your message after encryption is :{cipher_text}")

def decrypt(message,shift):
    caesar_text=""
    for m in message:
        if m in letter:
            position=letter.index(m)
            new_position=(position-shift)
            if(new_position<0):
                new_position=new_position+26
            final=new_position%26
            caesar_text+=letter[final]
        else:
            caesar_text+=m

    print(f" your message after decryption is :{caesar_text}")
        
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(letters)
end=False

while not end:
    choice=input("Type \" encrypt \" for encryption and \" decrypt\" for decryption:\n")
    message=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))

    if(choice=="encrypt"):
        encrypt(message,shift)
    elif(choice=="decrypt"):
        decrypt(message,shift)
    play_again=input("Type 'yes' to Continue , Type 'no' to exit:\n")
    if play_again=='no':
        end=True
        print("Have a nice day! Bye..")
         