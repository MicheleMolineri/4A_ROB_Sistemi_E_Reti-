def is_isogram(string):
    isogram , str =[], string.lower()
    for ch in str :
        if ch in isogram : return False
        elif ch not in ['-',' '] : isogram.append(ch) 
    return True
        
    
    

