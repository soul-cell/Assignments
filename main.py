if __name__ == "__main__":
    with open("sheet.csv", "r") as f:
        l1 = [i.strip("\n").split(',') for i in f]
        for item in l1:
            for value in item:
                if "?" in value:
                    item[item.index(value)] = value.replace("?", "")

        f1 = {l1[0][i]: [l1[j][i] for j in range(1, len(l1)) if l1[j][i] != '']
              for i in range(len(l1[0]))}
        ed = {i: f1[i] for i in f1 if i in ['Fresh vegetables', 'Condiments / Sauces', 'Baked goods', 'Fresh fruits']}
        ned = {i: f1[i] for i in f1 if i in ['Personal care', 'Cleaning products', 'Baby stuff']}
        d1 = {"edible": ed, "non-edible": ned}
        print(d1)


def filter_func():
    return


def view_menu():
    print(f"Menu\n{'-'*20}")
    print("1.Filters\n2.All_Items\n3.Exit")
    choice = int(input("Enter The Choice: "))
    if choice == 1:
        filter_func()
    elif choice == 2:
        print(f1)
    elif choice == 3:
        print("exit")
    else:
        print("exit")


# Code for Place Order
def place_order():
    return


# Code for get Previous order
def previous_order():
    return


def main():
    print(f"menu\n{'-'*20}")
    print("1.View Menu\n2.Place Orders\n3.Previous Orders\n4.Exit")
    select = int(input("Enter The Choice: "))
    if select == 1:
        view_menu()
    if select == 2:
        place_order()
    if select == 3:
        previous_order()
    if select == 4:
        print("Thanks For Coming!")


main()


def print_by_date(inp_date): #My function
    dict_collection = previous_orders()
    print("The items ordered on", inp_date, "are:", end=" ")
    print(dict_collection[inp_date])

user_date = input("enter the date-month-year:")
print_by_date(user_date)