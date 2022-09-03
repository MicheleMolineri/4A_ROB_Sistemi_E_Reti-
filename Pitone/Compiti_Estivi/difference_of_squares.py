
def square_of_sum(number):
    numbers = [ k for k in range(1,number+1)]
    return sum(numbers)**2
    
def sum_of_squares(number):
    numbs = [ k**2 for k in range(1,number+1)]
    return sum(numbs)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


