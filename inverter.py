reversed_alphabet = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A',
}

reversed_alphabet_with_mistakes = {
    'a': 'y',
    'b': 'z',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'm',
    'n': 'n',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'a',
    'z': 'b',
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'M',
    'N': 'N',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
}


def invert_character(character):
    # character = character.lower()
    if character in reversed_alphabet:
        return reversed_alphabet[character]
    else:
        return character


def invert_message(message):
    inverted = ""
    for char in message:
        inverted += invert_character(char)
    return inverted


m = "Gl Yibzmmz Yozmxl, Gsv rmgivkrw rmevhgrtzgli! Xirxp Xrgb'h qlfimzorhg uli qfhgrxv! Gl hl ivovmgovhhob slfmw lmv lu gsv irxsvhg urtfivh rm srhglib rh zm zxg lu uvziovhhmvhh. Dszg trug xlfow klhhryob vmxzkhfozgv hfxs wvgvinrmzgrlm, hfxs ulxfh! R kivhvmg gsv zmhdvi gszg gszg jfvhgrlm - drgs z krmxs lu kzmzxsv, lu xlfihv. Blfih rm giryfgv, Szizow Sziphrmt"
inverted_message = invert_message(m)
print(m)
print(inverted_message)
