
#10000 = Reverse the order of the operations in the secret handshake

actions = ["wink", "double blink", "close your eyes", "jump"]

def commands(code):
    code = int(code, 2)
    handshake = [a for i, a in enumerate(actions) if code & 1 << i]
    if code & 1 << 4:
        handshake = list(reversed(handshake))
    return handshake


print(commands("00011"))