def gcd(a,b):
    i=1
    div=0
    if a==0 or b==0:
        return "nil"
    while (i<a or i==a) and (i<b or i==b):
        
        if (a%i==0 and b%i==0):
            
            div=i
          
        i+=1
            
    return div

print(gcd(0,100))