def classify(number):
    '''
    Identify given natural number as perfect, abundant or deficient.
    :param number: must be positive integer (set natural numbers)
    :return: string 'perfect' or 'abundant' or 'deficient'
    '''
    if number < 1 or type(number) != int:
        raise ValueError(f'Given Number {number} is not in set of natural numbers!')
    else:
        f = [i for i in range (1,number) if number % i == 0]
        if sum(f) == number:
            return 'perfect'
        elif sum(f) > number:
            return 'abundant'
        else:
            return 'deficient'

print(classify(1))