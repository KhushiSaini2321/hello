def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    if b!=0:
        print(a//b)
    else:
        print("cannot divide by 0")
    
print("------------------simple calculator-----------------------")
print("choose operation")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")

choice = input("enter your choice (1/2/3/4) : ")
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

if choice == '1':
    print("result:" , add(num1 , num2))
elif choice == '2':
    print("result:", sub(num1, num2) )
elif choice =='3' :
    print("result: ", mul(num1, num2))
elif choice == '4' :
    print("result: ", div(num1, num2))
else:
    print("invalid input")