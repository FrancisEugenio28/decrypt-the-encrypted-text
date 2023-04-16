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
# Else just copy the char from the input then return the output
# print the output