# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
def shift_n(letter, n):
    if ord(letter)+n > ord('z'):
        pos = (ord(letter)+n) - ord('z') - 1
        return chr(ord('a') + pos)
    elif ord(letter)+n < ord('a'):
        pos = ord('a') - (ord(letter)+n) - 1
        return chr(ord('z') - pos)
    else:
        return chr(ord(letter) + n) 
        
def rotate(letter, n):
    # Your code here
    result = ''
    for _, char in enumerate(letter):
        if char.isalpha():
            result += shift_n(char, n)
        else:
            result += char
    return result    

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
