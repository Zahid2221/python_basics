# arguments and keyword arguments usage

def adding(n1,n2):
    return n1+n2
res=adding(10,20)
print('The sum  is ', res)

def addition(*args):
    sum=0
    for i in args:
        sum+=i
    print('sum of numbers is',sum)

addition(12,3,54,6)
addition(12,14,16,18,20)

# Now using keyword arguments



