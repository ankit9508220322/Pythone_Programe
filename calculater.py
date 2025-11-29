def add(a , b):
    return a + b;
def sub(a , b):
    return a-b;
def mul(a , b):
    return a * b;
def divid(a , b):
    return a / b;
def avg(a , b):
    return(a + b)/2;

print("* choes teh operation \n" 
     "1. addition \n"
     "2. subtraction\n"
     "3. multiply\n"
     "4. divide \n"
     "5. modular");

select =int(input("select the option 1 , 2 , 3 , 4 , 5 => "))

number1 = int(input("enter the number: "));
number2 = int(input("enter the number: "));

if select == 1:
    print("sum of two number is\n",add(number1 , number2));
    
elif select == 2:
    print("subtraction of 2 number: ",sub(number1 , number2));
elif select == 3:
    print("multiply of two number: ",mul(number1, number2));
elif select == 4:
    print("division of two number:  ",divid(number1, number2));
    
elif select == 5:
    print("mosule of value: ",avg(number1 , number2));

else:
    print("not valid option ");