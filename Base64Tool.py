import base64

encoding_type = 'utf-8'
# encoding_type = 'ascii'


def getMode():
    while True:
        print('B64 encode or decode')
        mode = input().lower()
        if mode in 'encode e decode d'.split():
            return mode
        else:
            print('Enter either "encode" or "e" or "decode" or "d".')


def is_read_file():
    print('Do you want to read from a file, or an input string?')
    mode = input().lower()
    if mode in 'file f'.split():
        return True
    else:
        return False


def getMessage():
    print('Enter your message:')
    return input()


def get_filename():
    print('Enter the filename:')
    return input()


def encode(message):
    message_bytes = message.encode(encoding_type)
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode(encoding_type)
    return base64_message


def decode(base64_message):
    base64_bytes = base64_message.encode(encoding_type)
    message_bytes = base64.b64decode(base64_bytes)
    decoded = message_bytes.decode(encoding_type)
    return decoded


def readFile(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    return lines

def readFileStripped(file_name):
    lines = readFile(file_name)
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    return stripped_lines

mode = getMode()
if is_read_file():
    filename = get_filename()
    for line in readFileStripped(filename):
        if mode[0] == 'd':
            output = decode(line)
        else:
            output = encode(line)
    print(output)
else:
    message = getMessage()
    if mode[0] == 'd':
        output = decode(message)
    else:
        output = encode(message)
    print(output)

