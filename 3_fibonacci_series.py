# Fibonacci Series
# a=1,b=2 ,c=a+b, a=b, b=c...  1,2,3,5,8,13...etc

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
how_many=int(input("How many number series you want: "))

print(f"🚀 {a} and {b} are the given inputs...")
for x in range(how_many):
    c=a+b
    a=b
    b=c
    print(c)