from datetime import date, datetime
if __name__ == "__main__":
    with open("sheet.csv", "r") as f:
        l1 = [i.strip("\n").split(',') for i in f]
        for item in l1:
            for value in item:
                if "? " in value:
                    item[item.index(value)] = value.replace("? ", "")

        f1 = {l1[0][i]: [l1[j][i] for j in range(1, len(l1)) if l1[j][i] != '']
              for i in range(len(l1[0]))}
        ed = {i: f1[i] for i in f1 if i in ['Fresh vegetables', 'Condiments / Sauces', 'Baked goods', 'Fresh fruits']}
        ned = {i: f1[i] for i in f1 if i in ['Personal care', 'Cleaning products', 'Baby stuff']}
        d1 = {"edible": ed, "non-edible": ned}
        print(d1)
        dict_collection = {}


def filter_func():
    print("Enter the choice of product:\n 1.Edible \n 2.Non-Edible")
    user_input = input("Enter the choice: ")
    if user_input == 1:
        for keys, val in d1["edible"].items():
            print(keys)
            print("-------------")
            for i in range(len(val)):
                print(i+1, val[i])
    elif user_input == 2:
        for keys, val in d1["non-edible"].items():
            print(keys)
            print("-------------")
            for i in range(len(val)):
                print(i+1, val[i])
    main()


def view_menu():
    print(f"Menu\n{'-'*20}")
    print("1.Filters\n2.All_Items\n3.Exit")
    choice = int(input("Enter The Choice: "))
    if choice == 1:
        filter_func()
    elif choice == 2:
        view_all_items()
    else:
        print("exit")
    main()


# Code for Place Order
def place_order():
    # global my_order
    # global today
    user_input_1 = input("Enter your comma(,) separated Order: ")
    my_order = [items for items in user_input_1.split(",")]
    today = date.today()
    time = datetime.now()
    print(f"Your Order is placed! Date:{time}s ")
    adder = input("Do you want to add more!, type : (yes/no): ")
    if adder == "yes":
        add = input("Enter your comma(,) separated  Order/s: ")
        new = [new for new in add.split(",")]
        my_order.extend(new)
        print(f"New item/s added,Order Placed!,Date:{time}s")
    valid_order = []
    for order in my_order:
        for dic in d1.values():
            for key, val in dic.items():
                if order in val:
                    print(f"{order} in {key}")
                    valid_order.append(order)
    for order in my_order:
        if order not in valid_order:
            print(f"{order} is  an incorrect product name/unavailable product.")
    previous_orders(today, my_order)
    main()


def previous_orders(d, order):
    if d not in dict_collection:
        dict_collection[d] = order
    else:
        dict_collection[d] = dict_collection[d] + order
    return dict_collection


def print_by_date(inp_date):
    print("The items ordered on", inp_date, "are:", end=" ")
    print(dict_collection[inp_date])
    main()


def view_all_items():
    for i, j in d1.items():
        print(i.upper())
        print("-----------------------")
        for k, v in j.items():
            print(k)
            print("------------------")
            for data in range(len(v)):
                print(data + 1, v[data])
    main()


def main():
    print(f"menu\n{'-'*20}")
    print("1.View Menu\n2.Place Orders\n3.Previous Orders\n4.Print by particular date\n5.Exit")
    select = int(input("Enter The Choice: "))
    if select == 1:
        view_menu()
    elif select == 2:
        place_order()
    elif select == 3:
        if dict_collection == {}:
            print("No orders yet ")
        else:
            print(dict_collection)
        main()
    elif select == 4:
        user_date = input("enter the year:month:date:")
        print_by_date(user_date)
    else:
        print("Thanks For Coming!")


main()
