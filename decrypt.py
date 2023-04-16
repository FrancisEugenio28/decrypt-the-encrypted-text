#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programming
#Problem 2: Lab Exercise 1

# Create a input for user
encrypt_str = input("What is the text that you are trying to decrypt?: ")
# Create a list of substitutions wherein this will be the basis of our program to decrypt the text
def decrypted_str(encrypted_str):
    decrypted_dict = {'*' : 'a', '&' : 'e', '#' : 'i', '+' : 'o', '!' : 'u'}
# Create an empty list wherein it accepts the decrypted text
    decrypt_str = ""    
# With the use of "For Loop", we command that every special text included in the input must be replace with their specific equivalent in the list of substitutions
    for char in encrypt_str:
        if char in decrypted_dict:
            decrypt_str += decrypted_dict[char]
# Else just copy the char from the input then return the output
    else:
            decrypt_str += char
    return decrypt_str
# print the output
print("Decryption Complete. Your Plain Text is " + decrypted_str(encrypt_str))