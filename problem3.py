#Check if a number is even or odf
#Check if there is a remainder after dividing by 2 if so then return false
#no edge cases needed to address

#if number remainder 2=0-return true
#else return false

def isEven(num):
    if num%2==0:
        return True
    else:
        return False
    
print(isEven(3))
print(isEven(4))