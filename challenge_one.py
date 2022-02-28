# 1.	Reverse a string
# a.	Write code that takes a string as input and returns the string reversed
# b.	i.e. “Hello” will be returned as “olleH”
# 2.	Capitalize letter
# a.	Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
# 3.	Compress a string of characters
# a.	For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
# 4.	BONUS CHALLENGE: Palindrome
# a.	A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b.	Write code that takes a user input and checks to see if it is a Palindrome and reports the result



from itertools import count


# def reverse_string(string_one):
#     print(f"{string_one}"[::-1]) #reverses string

# reverse = reverse_string("Hello")



# def capitalize_strings(string_two):
#     blank_space = " "
#     final_string = ""
#     for index in range(len(string_two)):

#         if string_two[index] is blank_space:
#             final_string += string_two[index+1].upper()
            
#         elif(string_two[index] != blank_space):
#             if string_two[index] is ".":
#                 print(final_string)
#                 break
#             final_string += string_two[index+1]

#         else:
#             print("Error")


# capitalize_first = capitalize_strings(" hello capital letter.")



# def compress_string(string_three):
#     letters = string_three
#     counter = 0
#     compressed_string = ""
#     previous_letter = string_three[0]
#     for current_letter in string_three:
#         if previous_letter == current_letter:
#             counter += 1
#         else:
#             compressed_string += previous_letter + str(counter)
#             counter = 1
#             previous_letter = current_letter
    
#     compressed_string += previous_letter + str(counter)
#     print(f"{compressed_string}")

# compression = compress_string("aaaabbccc")



def palindrome(palindrome_input):
    palindrome_input = input("enter a Palindrome: ")
    opposite = palindrome_input[::-1]
    is_it_palindrome = False
    while is_it_palindrome == False:
        if palindrome_input == opposite:
            print("Yes it is a palindrome!")
            is_it_palindrome = True

        else:
            print("Not a Palindrome, try again.")
            palindrome_input = input("enter a Palindrome: ")
            opposite = palindrome_input[::-1]



pal_check = palindrome("")