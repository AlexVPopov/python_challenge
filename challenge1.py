import string

alphabet = list(string.ascii_lowercase)

def alphabet_index(character):
    return alphabet.index(character)

def decoded_index(int):
    return (int + 2) % (len(alphabet))

def decoded_character(character):
    return alphabet[decoded_index(alphabet_index(character))]

def decode(coded_string):
    characters = list(coded_string)

    decoded_list = []

    for character in characters:
        if character in alphabet:
            decoded_list.append(decoded_character(character))
        else:
            decoded_list.append(character)

    return ''.join(decoded_list)

string_for_decoding = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(decode(string_for_decoding))

def next_url():
    return f"http://www.pythonchallenge.com/pc/def/{ decode('map') }.html"

print(next_url())
