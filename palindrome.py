#Input = 121
#Output = True

def palindrome(x):
    num_str = str(x)
    return num_str == num_str[::-1]

#Example
num = 121
if palindrome(num):
    print(f'{num} its a palindrome')
    
else:
    print(f'{num} its not a palindrome')