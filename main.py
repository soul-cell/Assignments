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



# Menu option is edited by jayasivan


def View_Menu():
    print("1.Filter\n2.All_Items\n3.Exit")
    choice = int(input("Enter The Choice: "))
    if choice == 1:
        return Filter()
    if choice == 2:
        "Code for get all item"
    if choice == 3:
        return main()


def Filter():
    print("1.Edible\n2.Non Edible")
    choice = int(input("Enter The Choice: "))
    if choice == 1:
        "Code for get edible"
    if choice == 2:
        "Code for get Non_edible"


def Place_Order():  # Code for Place Order
    return


def Previous_Order():  # Code for get Previous order
    return


def main():
    print("1.View Menu\n2.Place Orders\n3.Previous Orders\n4.Exit")
    choice = int(input("Enter The Choice: "))
    if choice == 1:
        View_Menu()
    if choice == 2:
        Place_Order()
    if choice == 3:
        Previous_Order()
    if choice == 4:
        print("Thanks For Coming!")


main()

