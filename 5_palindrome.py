def palindrome(n):
    rev=0
    temp=n
    while temp>0:
        r = temp%10
        temp//=10
        rev= rev*10+r
    return rev==n
    
print(palindrome(12136))