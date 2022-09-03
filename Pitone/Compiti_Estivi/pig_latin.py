"""Implement a program that translates from English to Pig Latin."""
def translate(text:str)->str:
    """
    Pig Latin is a made-up children's language that's intended to be confusing
    according to test cases
    """
    vowols = {'a','e','i','o','u'}
    words = text.split()
    res = []
    for word in words:
        if word.startswith('yt') or word.startswith('xr'):
            res.append(word + 'ay')
            continue
        ind = 0
        consonant = ''
        while ind<len(word):
            if word[ind] in vowols or (word[ind] == 'y' and consonant!=''):
                res.append(word[ind:]+consonant+'ay')
                break
            if word[ind] == 'q' and word[ind+1] == 'u':
                consonant += 'qu'
                ind += 1
            else:
                consonant += word[ind]
            ind += 1
    return ' '.join(res)
