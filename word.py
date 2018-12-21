def new(number,loop):
    if loop==1:
        return number
    else:
        return number*new(number,loop-1)
a=new(5,5)
print a
print "Hello"*a
