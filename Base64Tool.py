import base64

def getMode():
    while True:
        print('B64 encode or decode')
        mode = input().lower()
        if mode in 'encode e decode'.split():
            return mode
        else:
            print('Enter either "encode" or "e" or "decode" or "d".')


def getMessage():
    print('Enter your message:')
    return input()


def encode(message):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def decode(base64_message):
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    decoded = message_bytes.decode('utf-8')
    return decoded


mode = getMode()
message = getMessage()
if mode[0] == 'd':
    output = decode(message)
else:
    output = encode(message)

print(output)
