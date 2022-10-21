# encryption.py
# Joshua Jipp, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.
import string


### Define your functions here


def message_encoder(text_to_encode, user_cipher_input):
    """
    takes user input for the prompt they want to encode and uses the user cipher input to encode the message. 
    Arguments:
    text_to_encode -- this is a user inputed string that will be encoded
    user_cipher_input -- user inputed string which is used to determine how the prompt will be encoded

    Returns:
    encoded_text -- The function will run and return the encoded text
    """   
    dict_keys = string.ascii_lowercase
    cipher_dict = dict(zip(dict_keys, user_cipher_input))
    encoded_text = ''
    n = 0
    while n < (len(text_to_encode)):
        if text_to_encode[n] in cipher_dict:
            encoded_text += cipher_dict.get(text_to_encode[n])
        n = n + 1
    return encoded_text

def message_decoder(text_to_decode, user_cipher_input):
    """
    takes user input for the prompt they want to decode and uses the user cipher input to decode the message. 
    Arguments:
    text_to_encode -- this is a user inputed string that will be decoded
    user_cipher_input -- user inputed string which is used to determine how the prompt will be decoded

    Returns:
    decoded_user_text -- The function will run and return the decoded text
    """
    dict_keys = string.ascii_lowercase
    cipher_dict = dict(zip(user_cipher_input, dict_keys))
    decoded_user_text = ''
    n = 0
    while n < (len(text_to_decode)):
        if text_to_decode[n] in cipher_dict:
            decoded_user_text = decoded_user_text + cipher_dict.get(text_to_decode[n])
        n = n + 1
    return decoded_user_text

def is_cipher_valid(input_cipher):
    """
    function is used to check if the user cipher is valid. If the cipher is invalid, it will tell the user that the cipher cipher must contain 26 unique elements of a-z or 0-9.
    If the user cipher text is valid, it will print "Your cipher text is valid" and will return final_cipher_result.

    Arguments:
    input_cipher -- this is the cipher that the user inputed. It will be checked for validity.

    Returns:
    final_cipher_result -- retruns the user inputted cipher if the cipher text is valid
    False -- function will return False if any of the first while loop conditions are met
    
    """
    lowercase_cipher = input_cipher.lower()
    lowercase_cipher = list(dict.fromkeys(lowercase_cipher))

    final_cipher_result = ''
    for n in lowercase_cipher:
        final_cipher_result = final_cipher_result + n
    while (len(final_cipher_result)) != (len(set(final_cipher_result))):
        print('Your cipher must contain 26 unique elements of a-z or 0-9')
        return False
    while (len(final_cipher_result) != 26):
        print('Your cipher must contain 26 unique elements of a-z or 0-9')
        return False
    while not (final_cipher_result.isalnum()):
        print('Your cipher must contain 26 unique elements of a-z or 0-9')
        return False
    else:
    #     print('Your cipher text is valid.')
        return final_cipher_result

print("ENDG 233 Encryption Program")
user_input = -1


### Add your main program code here

while user_input != 0:                                                           #while loop will run if user_input is not 0
    user_input = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) #asks the user to input a number to encode or decode a message, or to quit the program 
    if user_input == 1:                                                              # if the user_input is 1, this branch will execute
        user_prompt_input = input('Please enter the text to be processed: ') #asks the user to input a prompt that they want encoded
        user_input_cipher = input('Please enter the cipher text: ')             # asks the user to enter a valid cipher
        if (is_cipher_valid(user_input_cipher) != False):                           #calls the "is_cipher_valid" function and if the function cipher text is valid, this branch will be executed
            print('Your cipher is valid.')
            print('Your output is:', message_encoder(user_prompt_input, is_cipher_valid(user_input_cipher)))   #prints the encoded message
    
    elif user_input == 2:                                                       # if the user_input is 1, this branch will execute
        user_prompt_input = input('Please enter the text to be processed: ')    #asks the user to input a prompt that they want decoded
        user_input_cipher = input('Please enter the cipher text: ')              # asks the user to enter a valid cipher
        if (is_cipher_valid(user_input_cipher) != False):                          #calls the "is_cipher_valid" function and if the function cipher text is valid, this branch will be executed
            print('Your cipher is valid.')
            print('Your output is:', message_decoder(user_prompt_input, is_cipher_valid(user_input_cipher)))  #prints the decoded message

print('Thank you for using the encryption program.')        #once the while loop is exited, the program will print "Thank you for using the encryption program."

