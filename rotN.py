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

def rotN_force_dec(message):
    for n in range(23):
        print("Decode N: " + str(n))
        rotn_alpha_dec = rot_alpha(n * -1)
        dec = rotn_alpha_dec(message)
        print("\t" + dec)


def get_rot_47_chars():
    global join
    chars = []
    for x in range(33, 127):
        char = chr(x)
        chars.append(char)
    join = "".join(chars)
    return join

m = "Gl Yibzmmz Yozmxl, Gsv rmgivkrw rmevhgrtzgli! Xirxp Xrgb'h qlfimzorhg uli qfhgrxv! Gl hl ivovmgovhhob slfmw lmv lu gsv irxsvhg urtfivh rm srhglib rh zm zxg lu uvziovhhmvhh. Dszg trug xlfow klhhryob vmxzkhfozgv hfxs wvgvinrmzgrlm, hfxs ulxfh! R kivhvmg gsv zmhdvi gszg gszg jfvhgrlm - drgs z krmxs lu kzmzxsv, lu xlfihv. Blfih rm giryfgv, Szizow Sziphrmt"
rotN_force_dec(m)
