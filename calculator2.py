try:
    a = float(input("enter the first number: "));
    b = float(input("enter the second number: "));
    print("choes the operation (+,_,*,/):")
    op = input("enter the operation")
    match op:
        case "+":
            print(f"the addition is=: {a + b}");
        case "-":
            print(f"the subtraction is= {a - b}");
        case "*":
            print(f"the multiplication is= {a * b}");
        case "/":
            print(f"the division is= {a / b}");
        case default:
            print(f"invild operation ")
except Exception as e:
    print("inyrt the valid value of a and b");
    