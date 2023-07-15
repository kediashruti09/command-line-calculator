#code for CLI calculator
import argparse
import math


        #perform a calculation based on user input

parser = argparse.ArgumentParser(description ='Take two integer or float value-')
parser.add_argument("num1",type=float,help='give a positive value for first variable')
parser.add_argument("num2",type=float,help='give a positive value for second variable')
parser.add_argument("operation",choices=['+','-','*','/','max','min','min','log','power','square root','gcd'],help="the operation must be +,-,*,/,log,max,min,square root,gcd")
args = parser.parse_args()
num1= args.num1
num2=args.num2
operation=args.operation
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




   
