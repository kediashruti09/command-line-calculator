#code for cli calculator
import math
num1=float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))
operation =input("choose the operation(+,-,*,/,max,min,log,power,square root,gcd):")

        #perform calculation based on user input

if operation == "+":
    result = num1+num2
    print(round(result,3))
elif operation =="-":
    result = abs(num1-num2)
    print(round(result,3))
elif operation == "*":
    result = num1*num2
    print(round(result,3))
elif operation == "/":
    if num2!=0 and num1!=0:
        result = num1/num2
        print(round(result,3))
    elif num2==0:
        print("invalid number")
    elif num1==0:
        result=num1%num2
        print(round(result,3))
elif operation == "max":
    result = max(num1,num2)
    print(round(result,3))
elif operation == "min":
    result= min(num1,num2)
    print(round(result,3))
elif operation == "power":
    result=math.pow(num1,num2)
    print(round(result,3))
elif operation == "log":
    if num1>0 and num2>0:
        result1=math.log(num1,num2)
        print(round(result1,3))
        result2=math.log(num2,num1)
        print(round(result2,3))
    else:
        print("invalid number entered")
elif operation == "square root":
    if num1 >=0 and num2 >=0:
        result1=math.sqrt(num1)
        print(round(result1,3))
        result2=math.sqrt(num2)
        print(round(result2,3))
    elif num1>=0 and num2<0:
        result1=math.sqrt(num1)
        print(round(result1,3))
        result2=math.sqrt(abs(num2))
        print(str(round(result2,3))+"i")
    elif num1<0 and num2>=0:
        result1=math.sqrt(abs(num1))
        print(str(round(result1,3))+"i")
        result2=math.sqrt(num2)
        print(round(result2,3))
    elif num1<0 and num2<0:
        result1=math.sqrt(abs(num1))
        print(str(round(result1,3))+ "i")
        result2=math.sqrt(abs(num2))
        print(str(round(result2,3))+"i")
    
elif operation == "gcd":
    result=math.gcd(int(num1),int(num2))
    print(result)
else:
    print("invalid operation")



