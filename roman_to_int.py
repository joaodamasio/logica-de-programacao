#input = 'MCMLIV'
#output = '1954'

def roman_to_integer(roman):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    before = 0
    
    #Run a roman number of the rigth to left
    for algorism in roman[::-1]:
        val = roman_to_int[algorism]
        
        #If the current value is lower than the previous one, subtract
        if val < before:
            total -= val
            
        else:
            total += val
        before = val
        
    return total

number_roman = 'MCMLIV'
print(roman_to_integer(number_roman))