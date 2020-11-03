import string

MAX_KEY_SIZE = 26

def number_to_letter(number_input):
    output = ""
    list_of_characters = list(string.ascii_letters)

    for character in number_input:
        val = list_of_characters[int(character)-1]
        output = str(output) + str(val)
    print(output)


print('Write Text: ')
input_text = input().lower().split(" ")
number_to_letter(input_text)