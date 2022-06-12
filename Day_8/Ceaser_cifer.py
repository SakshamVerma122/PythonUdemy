alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher_encode(text,shift):
    for char in text:
        if(char.isalpha()):
            index = alphabet.index(char)
            index += shift
            index %= len(alphabet)
            print(alphabet[index],end='')
        else:
            print(char,end='')
    print()

def ceaser_cipher_decode(text,shift):
    print("Here's the encoded result: ")
    for char in text:
        if(char.isalpha()):
          index = alphabet.index(char)
          index -= shift
          print(alphabet[index],end='')
        else:
          print(char,end='')
    print()
  



command = 'yes'
while(command == 'yes'):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
  text = input("Type your message:\n").lower()
  
  shift = int(input("Type the shift number:\n"))
  
  if(direction == 'encode'):
    ceaser_cipher_encode(text,shift)
  else:
    ceaser_cipher_decode(text,shift)
    
  print("Type 'yes' if you want to go again. Otherwise type 'no'.")
  
  command = input()

