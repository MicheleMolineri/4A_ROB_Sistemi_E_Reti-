"""has 3 as a factor, add 'Pling' to the result.
has 5 as a factor, add 'Plang' to the result.
has 7 as a factor, add 'Plong' to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
"""

def convert(number):

    s , sounds ,index= "" , ['Pling','Plang','Plong'],0

    for mod in range(3,8,2):
        if number % mod == 0 :
            s+=sounds[index]
        index+=1

    if s == "" : return str(number)
    else : return s

print(convert(28))
