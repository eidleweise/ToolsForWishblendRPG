def letter_to_number(input_text):
    output = []
    for character in input_text:
        number = ord(character) - 96
        output.append(number)
    print(output)


print('Write Text: ')
input_text = input().lower()
letter_to_number(input_text)
