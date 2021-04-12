# Import the groupby function from itertools, 
# this takes any sequence and returns an array of groups by some key
from itertools import groupby

# Use a dictionary as a lookup table
dailpad = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' '],
}


def phone_pad(input_str):
    # Convert to string if given a number
    if (input_str.isnumeric()):
        if type(input_str) == int:
            input_str = str(input_str)

        # Create our string output for the dialed numbers
        output = ''

        # Group each set of numbers in the order
        # they appear and iterate over the groups.
        # (eg. 222556 will result in [(2, [2, 2, 2]), (5, [5, 5]), (6, [6])])
        # We can use the second element of each tuple to find
        # our index into the dictionary at the given number!
        for number, letters in groupby(input_str):
            # Convert the groupby group generator into a list and
            # get the offset into our array at the specified key
            offset = len(list(letters)) - 1

            # Check if the number is a valid dialpad key (eg. 1 for example isn't)
            if number in dailpad.keys():
                # Add the character to our output string and wrap
                # if the number is greater than the length of the character list
                output += dailpad[number][offset % len(dailpad[number])]
            else:
                raise ValueError(f'Unrecognized input "{number}"')

        return output
    else:
        print("input was text " + input_str)
        output = ''
        for letter in input_str:
            for key, value in dailpad.items():
                #print(key, value)
                if letter in value:
                    index = 0
                    for l in value:
                        index = index + 1
                        output = output + key
                        if letter == l:
                            break

        return output


print('Write Text: ')
input_text = input().lower()
pad = phone_pad(input_text)
print(pad)

