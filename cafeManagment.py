num = {
    'piza':40,
    'pasta':20,
    'burger':30,
    'manchuriyan':40,
    'samosa':20,
    'coffe':35
};
print("welcome to my shope $ cafe");
print("piza:RS40\npasta: RS20\nburger: RS30\nmanchuriyam: Rs40:\nsamosa: Rs20:\ncoffe: Rs25");
order_total = 0;
item =input("enter the name of item this menu ");
if item in num:
    order_total+=num[item]
    print(f"your item was input {item} please wait some time");
else:
    print(f"your order dont match {item} this menu");
    
another_order = input("do you want too another order(YES/no)");
if another_order =="yes":
    item2 = input("enter the name of  second order = ");
    if item2 in num:
        order_total +=num[item2]
        print(f"item {item2} has ben add this order");
    else:
        print(f"order not {item2}found this menu");
print(f"the total amount of item {order_total}")