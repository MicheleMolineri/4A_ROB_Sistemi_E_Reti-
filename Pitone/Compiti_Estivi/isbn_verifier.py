def is_valid(isbn):
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    r = 0
    for i in range(10):
        try:
            r += int(isbn[i]) * (10-i)
        except ValueError:
            return False
    return r % 11 == 0

print(is_valid("3-598-21508-8"))