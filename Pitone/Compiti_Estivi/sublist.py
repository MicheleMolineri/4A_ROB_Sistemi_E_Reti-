SUBLIST =   'SUBLIST'
EQUAL =     'EQUAL'
SUPERLIST = 'SUPERLIST'
UNEQUAL =   'UNEQUAL'
import re

def sublist(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    
    if len(first_list) < len(second_list):
        smaller =  ','.join(str(item) for item in first_list)
        larger  =  ','.join(str(item) for item in second_list)
    
    else:
        smaller =  ','.join(str(item) for item in second_list)
        larger  =  ','.join(str(item) for item in first_list) 
    
    to_match = re.compile(smaller)
    matched = to_match.search(larger)
    
    if matched:
        return SUBLIST if matched.group() == ','.join(str(item) for item in first_list) else SUPERLIST
    
    return UNEQUAL