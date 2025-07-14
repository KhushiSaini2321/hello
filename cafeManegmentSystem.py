#mini project
#cafe manegment system
print("-----------------------------------CAFE MANEGMENT SYSTEM-------------------------------------")
menu = {
    "pasta" : 60,
    "coffee" : 80,
    "burger" : 70,
    "coke" : 80,
    "pizza" : 120
}
print("-----------------------------------hey sir/Madam, good morning, welcome to are cafe-----------")
print("pasta : 60, \ncoffee : 80,\n burger : 70,\ncoke : 80,\n pizza : 120")
order_total = 0
item_1 = input("enter the name of item you went to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"ordered item{item_1} has been addede to your order")
else :
    print(f"ordered item{item_1}not valid yet!")

another_order = input("do you went anything else")
if another_order == "Yes":
    item_2 = input("enter the name of item you went to order =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"ordered item{item_2} has been addede to your order=
            ")
    else :
        print(f"ordered item{item_2}not valid yet!")

print(f"the total amount of your items is to pay{order_total}")
