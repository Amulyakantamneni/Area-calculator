#!/usr/bin/env python
# coding: utf-8

# # <center>PGP Data Science Engineering</center>
# ## <center>Introduction to Programming – Mini Project:</center>
# 

# ### Problem 1:
# 
# 1. Write a program to calculate area of shapes. Your program should be capable of calculating the area of a square, rectangle, triangle and a circle. The user should be presented with options to select the shape. Based on which shape is chosed by the user, the program should ask for the appropriate input and print the resulting area on the screen.
# 
# When the program is run, the screen should display something like this:
# 
# **Which shape would you like to calculate the area for? Please enter the option number-**<br>
# **1. Square**<br>
# **2. Rectangle**<br>
# **3. Triangle**<br>
# **4. Circle**<br>
# **Enter Option: _**
# 
# Say the user enters the option 1.
# 
# **Please enter the length of a side: _**
# 
# If the user enters a value of 5. The output should be:
# 
# **The area of the square is 25**
# 
# This program should indicate that the input is invalid if the user enters a character instead of a number as input. For instance if the user enters a value of ‘a’ instead of 5 in the previous example the program should prompt:
# 
# **Invalid input, please enter a number: _**
# 

# In[1]:


def inputNumber(prompt):
    s = input(prompt)
    
    while not s.isnumeric():
        s = input("Invalid input, please enter a number: ")
        
    print()
    return int(s)
    
    
def calculateAreaOfShape():
    print("Which shape would you like to calculate the area for? Please enter the option number-")
    print("1. Square")
    print("2. Rectangle")
    print("3. Traingle")
    print("4. Circle")
    
    opt = int(input("Enter Option: "))
    
    print()
    if opt == 1:
        length = inputNumber("Please enter the length of the square: ")
        area = length * length
        print("The area of the square is", area)
        
    elif opt == 2:
        length = inputNumber("Please enter the length of the rectangle: ")
        breadth = inputNumber("Please enter the breadth of the rectangle: ")
        area = length * breadth
        print("The area of the rectangle is", area)
        
    elif opt == 3:
        base = inputNumber("Please enter the base of the triangle: ")
        height = inputNumber("Please enter the height of the triangle: ")
        area = 0.5 * base * height
        print("The area of the triangle is", area)
        
    elif opt == 4:
        radius = inputNumber("Please enter the radius of the circle: ")
        area = 3.14 * radius * radius
        print("The area of the circle is", area)
        
    else:
        print("Invalid Option")
    
calculateAreaOfShape()


# ### Problem 2:
# 
# Create and encrypter in python based on the ceaser cipher. It is a substitution cipher where each character of the original text is shifted a certain number characters in the alphabet. Write a function that would require 2 arguments – the input text to be encrypted and a key. For eg: Given the input text ‘hello’ and the key 3, the resulting encryted text would be ‘khoor’. Here you can see that every character in the string hello is shifted by 3 characters. ‘h’ has shifted to ‘k’, ‘e’ has shifted to ‘h’ and so on. If a key of 5 were used, the resulting string would be ‘mjqqt’. This function should be capable of ignoring any characters which are not alphabets. Th2 character ‘z’ entered b
# y the user for a key of 3 would result in ‘c’.
# 
# Usage:<br>
# **encrypt(‘hello world!’, 3)**<br>
# **‘khoor zruog!’**
# 
# Similarly create decrypter which can decode the encryted text when provided the input text and key
# 
# Usage:<br>
# **decrypt(‘khoor zruog!’, 3)**<br>
# **‘hello world!’**
# 
# For the sake of simplicity you can assume that input solely consists of lowercase alphabets, spaces and punctuation symbols. Numbers in the input text would also be ignored similar to symbols.

# In[1]:


alphabet = list('abcdefghijklmnopqrstuvwxyz')

def encrypt(text, key):
    encrypted_text = ''
    
    for char in text:
        if char.isalpha():
            # shift each char right by key and wrap around the length of the alphabet
            encrypted_char_index = (alphabet.index(char) + key) % len(alphabet)
            encrypted_char = alphabet[encrypted_char_index]
            encrypted_text = encrypted_text + encrypted_char
        else:
            encrypted_text = encrypted_text + char
            
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ''
    
    for char in text:
        if char.isalpha():
            # shift each char left by key and wrap around the length of the alphabet
            decrypted_char_index = (alphabet.index(char) - key) % len(alphabet)
            decrypted_char = alphabet[decrypted_char_index]
            decrypted_text = decrypted_text + decrypted_char
        else:
            decrypted_text = decrypted_text + char
            
    return decrypted_text

print(encrypt('hello world!', 3))
print(decrypt('khoor zruog!', 3))

