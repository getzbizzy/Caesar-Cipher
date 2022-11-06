import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_char = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/1234567890 """)

play_again = True
    
def caeser(message, shift_num, cipher_direction):
    if cipher_direction == "encode":
      encoded_word = ""
      for letter in message:
        if letter in special_char:
          encoded_word += letter
        elif alphabet.index(letter) + shift_num >= 26:
          new_ndx = alphabet.index(letter) - 26 + shift_num
          encoded_letter = alphabet[new_ndx]
          encoded_word += encoded_letter 
        else:
          new_ndx = alphabet.index(letter) + shift_num
          encoded_letter = alphabet[new_ndx]
          encoded_word += encoded_letter 
      print(f"The encoded text is: {encoded_word}")
    elif cipher_direction == "decode":
      decoded_word = ""
      for letter in message:
        if letter in special_char:
          decoded_word += letter
        else:
          new_ndx = alphabet.index(letter) - shift_num
          decoded_letter = alphabet[new_ndx]
          decoded_word += decoded_letter
      print(f"The decoded text is: {decoded_word}")

answer = "y"

while play_again:
  if answer.lower() == "n":
    play_again == False
    print("Goodbye.")
    break
  elif answer != "y":
    input("Invalid answer. Press enter to continue...")
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if play_again == False:
    print("Goodbye.")
  elif play_again == True:
    if shift > 26:
      shift = shift % 26 
    caeser(message=text, shift_num=shift, cipher_direction=direction)
    answer = input("Do you want to play again? y/n\n")