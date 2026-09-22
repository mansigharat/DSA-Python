def palindrome(n):
    add = 0
    product=1
    temp=n
    while temp>0:
        r = temp%10
        temp//=10
        add += r
        product *= r
    return product-add
    
print(palindrome(34620))