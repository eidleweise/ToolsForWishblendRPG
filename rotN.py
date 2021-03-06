from string import ascii_lowercase, ascii_uppercase


def rot(*symbols):
    def _rot(n):
        encoded = ''.join(sy[n:] + sy[:n] for sy in symbols)
        lookup = str.maketrans(''.join(symbols), encoded)
        return lambda s: s.translate(lookup)
    return _rot


rot5_num = rot('0123456789')(5)
rot5_num('1234') # 6789

rot_alpha = rot(ascii_lowercase, ascii_uppercase)
rotn_alpha_enc = rot_alpha(13)
rotn_alpha_dec = rot_alpha(-13)


def get_rot_47_chars():
    global join
    chars = []
    for x in range(33, 127):
        char = chr(x)
        chars.append(char)
    join = "".join(chars)
    return join


rot_47 = rot(get_rot_47_chars())
rot_47_enc = rot_47(47)
rot_47_dec = rot_47(-47)


# enc = rotn_alpha_enc('Hello World') # Mjqqt Btwqi
# print(enc)
# dec = rotn_alpha_dec(enc)
# print(dec)

enc = rot_47_enc('Hello World') # Mjqqt Btwqi
print(enc)
dec = rot_47_dec(enc)
print(dec)