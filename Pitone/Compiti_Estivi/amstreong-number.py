def is_armstrong_number(number):
    
    total=0
    
    for figure in str(number) :
        total += int(figure)**len(str(number))

    if total == number : return True
    else : return False