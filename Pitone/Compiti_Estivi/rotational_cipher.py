ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    encrypted_text = ""
    for c in text:
        if c.isalpha():
            shifted = get_cipher(c.lower(), key)
            # preserve uppercase letters
            if c.isupper():
                encrypted_text += shifted.upper()
            else:
                encrypted_text += shifted
        else:
            # spaces and numbers
            encrypted_text += c
    return encrypted_text
def get_cipher(c, key):
    idx = ALPHA.index(c)
    shift = idx + int(key)
    if shift >= 26:
        shift -= 26
    return ALPHA[shift]