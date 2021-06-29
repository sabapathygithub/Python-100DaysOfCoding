from caesar_cipher import caeser_chiper_art


def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for char in plain_text:
        ind = alphabet.index(shift_amount)
        shift_ind = ind + shift
        if shift_ind < len(alphabet):
            encoded_text += alphabet[shift_ind]
        else:
            mod_ind = shift_ind - len(alphabet)
            encoded_text += alphabet[mod_ind]
    print(f"The encoded text is {encoded_text}")


def decrypt(encoded_text, un_shift):
    decoded_text = ""
    for char in encoded_text:
        ind = alphabet.index(char)
        shift_ind = ind - un_shift
        decoded_text += alphabet[shift_ind]
    print(f"The decode text is {decoded_text}")


# The below function is the outcome of merging the above two function.
def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position < len(alphabet):
            output_text += alphabet[new_position]
        else:
            mod_ind = new_position - len(alphabet)
            output_text += alphabet[mod_ind]
    print(f"Here's the {direction}d result: {output_text}")


if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    go_again = "yes"
    print(caeser_chiper_art.logo)
    while go_again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text, shift, direction)
        go_again = input("Type 'Yes' if you want to go again. Otherwise type 'no'").lower()
