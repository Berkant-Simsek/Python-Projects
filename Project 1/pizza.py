import csv
from datetime import datetime

def main():

    menu = open("Menu.txt", "r")
    menu_information = menu.read().splitlines()
    menu_pizza_types = []
    menu_pizza_sauce = []
    menu_pizza_types[0:4] = menu_information[1:5]
    menu_pizza_sauce[0:6] = menu_information[6:12]


    class menu:
        def __init__(self, name, prize):
            self.name = name
            self.prize = prize
        def get_info(self):
            print("The prize is " + str(self.prize))
            print("")
        def get_name(self):
            return self.name
        def get_prize(self):
            return self.prize

    class sauce_type(menu):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print("The prize of " + self.name + " is " + str(self.prize) + " TL.")
            print("If you want extra, the prize is " + str(1.5 * self.prize) + " TL.")
            print("")

    class pizza_type(menu):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print(self.name + " include this pizza toppings:")
            print("")
            print("And the prize is " + str(self.prize) + " TL.")
            print("")
        def get_prize(self):
            return self.prize

    class classic(pizza_type):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print(self.name + " include this pizza toppings:")
            print("Sausage, salami, corn, green and red pepper, cheese")
            print("And the prize is " + str(self.prize) + " TL.")
            print("")
    class margherita(pizza_type):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print(self.name + " include this pizza toppings:")
            print("Tomato, mozarella, basil, olive oil, salt")
            print("And the prize is " + str(self.prize) + " TL.")
            print("")
    class turkpizza(pizza_type):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print(self.name + " include this pizza toppings:")
            print("Mince, gravy, green and red pepper, oil")
            print("And the prize is " + str(self.prize) + " TL.")
            print("")
    class plainpizza(pizza_type):
        def __init__(self, name, prize):
            super().__init__(name, prize)
        def get_info(self):
            print(self.name + " include this pizza toppings:")
            print("Tomato, red pepper, ketchup")
            print("And the prize is " + str(self.prize) + " TL.")
            print("")


    def select_pizza():
        a = []
        x = 0
        while(x==0):
            selected_pizza = input("Please select a Pizza type. (Please just write the Pizza type and if you don't want any other pizza enter 0): ").lower()
            if(selected_pizza == ""):
                print("You didn't select Pizza type in the menu!")
            elif(str(last_selected[0][0]).lower() == selected_pizza) or (str(last_selected[1][0]).lower() == selected_pizza) or (str(last_selected[2][0]).lower() == selected_pizza) or (str(last_selected[3][0]).lower() == selected_pizza):
                print("You already select this pizza!")
            else:
                match(selected_pizza):
                    case "turkpizza":
                        number_of_pizza("TurkPizza")
                        number = pizza_numbers[0]
                        a = ["TurkPizza", number]
                        return a
                    case "plainpizza":
                        number_of_pizza("PlainPizza")
                        number = pizza_numbers[0]
                        a = ["PlainPizza", number]
                        return a
                    case "margherita":
                        number_of_pizza("Margherita")
                        number = pizza_numbers[0]
                        a = ["Margherita", number]
                        return a
                    case "classic":
                        number_of_pizza("Classic")
                        number = pizza_numbers[0]
                        a = ["Classic", number]
                        return a
                    case "0":
                        return a
                    case _:
                        print("You didn't select Pizza type in the menu!")


    pizza_numbers = [0]
    def number_of_pizza(x):
        try:
            number = int(input("How many " + x + " pizza do you want? (Please write number): "))
        except Exception:
            print("You entered invalid value!")
            number_of_pizza(x)
        else:
            if(number > 0):
                pizza_numbers.clear()
                pizza_numbers.append(number)
            else:
                print("You can't select 0 and negative number.")
                number_of_pizza(x)


    def select_sauce_q(aa):
        ans = input("Do you want sauce? (y/n): ").lower()
        match(ans):
            case "y":
                select_sauce(aa)
                return 1
            case "n":
                return 0
            case _:
                print("Invalid input!")
                select_sauce_q(aa)


    def extra_sauce():
        ans = input("Do you want extra? (y/n): ").lower()
        match(ans):
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Invalid input!")
                extra_sauce()


    sauces = []
    def select_sauce(aa):
        x = 0
        while(x == 0):
            selected_sauce = input("Which sauce or sauces do you want? (Please just write the sauce type in order and if you done selecting enter 0): ").lower()
            match(selected_sauce):
                case "olives" | "olive":
                    if((["Olives", True] in sauces) or (["Olives", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["Olives", True])
                        else:
                            sauces.append(["Olives", False])
                case "mushrooms" | "mushroom":
                    if((["Mushrooms", True] in sauces) or (["Mushrooms", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["Mushrooms", True])
                        else:
                            sauces.append(["Mushrooms", False])
                case "goatcheese":
                    if((["GoatCheese", True] in sauces) or (["GoatCheese", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["GoatCheese", True])
                        else:
                            sauces.append(["GoatCheese", False])
                case "meat":
                    if((["Meat", True] in sauces) or (["Meat", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["Meat", True])
                        else:
                            sauces.append(["Meat", False])
                case "onions" | "onion":
                    if((["Onions", True] in sauces) or (["Onions", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["Onions", True])
                        else:
                            sauces.append(["Onions", False])
                case "corn":
                    if((["Corn", True] in sauces) or (["Corn", False] in sauces)):
                        print("You already selected this sauces!")
                    else:
                        ans = extra_sauce()
                        if(ans):
                            sauces.append(["Corn", True])
                        else:
                            sauces.append(["Corn", False])
                case "0":
                    x = 1
                case _:
                    print("You didn't select sauce type in the menu!")    
        if(sauces == []):
            return 1
        else:
            add(aa, sauces)
            sauces.clear()


    def add(aa, sauces):
        try:
            number = int(input("How many " + last_selected[aa][0] + " pizzas would you like to add to? (Please just write number): "))
        except Exception:
            print("You entered invalid value!")
            add(aa, sauces)
        else:
            if(number > 0 and number <= (last_selected[aa][1])):
                num = last_selected[aa][1] - number
                if(num == 0):
                    last_selected[aa][1] = num
                    match(aa):
                        case 0:
                            return last_selected0.append([last_selected[aa][0], number, *sauces])
                        case 1:
                            return last_selected1.append([last_selected[aa][0], number, *sauces])
                        case 2:
                            return last_selected2.append([last_selected[aa][0], number, *sauces])
                        case 3:
                            return last_selected3.append([last_selected[aa][0], number, *sauces])
                else:
                    last_selected[aa][1] = num
                    match(aa):
                        case 0:
                            last_selected0.append([last_selected[aa][0], number, *sauces])
                        case 1:
                            last_selected1.append([last_selected[aa][0], number, *sauces])
                        case 2:
                            last_selected2.append([last_selected[aa][0], number, *sauces])
                        case 3:
                            last_selected3.append([last_selected[aa][0], number, *sauces])
                    sauces.clear()
                    print("For the rest of " + last_selected[aa][0] + " pizzas:")
                    select_sauce_q(aa)
            else:
                print("You can't select 0, negative number and over the selected pizza number.")
                add(aa, sauces)


    def sauce_prize0(i, prize1):
        if("Olives" in last_selected0_sauces[i]):
            if(["Olives", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Olives.get_prize())
            else:
                prize1 = prize1 + Olives.get_prize()
        if("Mushrooms" in last_selected0_sauces[i]):
            if(["Mushrooms", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Mushrooms.get_prize())
            else:
                prize1 = prize1 + Mushrooms.get_prize()
        if("GoatCheese" in last_selected0_sauces[i]):
            if(["GoatCheese", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * GoatCheese.get_prize())
            else:
                prize1 = prize1 + GoatCheese.get_prize()
        if("Meat" in last_selected0_sauces[i]):
            if(["Meat", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Meat.get_prize())
            else:
                prize1 = prize1 + Meat.get_prize()
        if("Onions" in last_selected0_sauces[i]):
            if(["Onions", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Onions.get_prize())
            else:
                prize1 = prize1 + Onions.get_prize()
        if("Corn" in last_selected0_sauces[i]):
            if(["Corn", True] == last_selected0_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Corn.get_prize())
            else:
                prize1 = prize1 + Corn.get_prize()
        return prize1
    def sauce_prize1(i, prize1):
        if("Olives" in last_selected1_sauces[i]):
            if(["Olives", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Olives.get_prize())
            else:
                prize1 = prize1 + Olives.get_prize()
        if("Mushrooms" in last_selected1_sauces[i]):
            if(["Mushrooms", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Mushrooms.get_prize())
            else:
                prize1 = prize1 + Mushrooms.get_prize()
        if("GoatCheese" in last_selected1_sauces[i]):
            if(["GoatCheese", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * GoatCheese.get_prize())
            else:
                prize1 = prize1 + GoatCheese.get_prize()
        if("Meat" in last_selected1_sauces[i]):
            if(["Meat", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Meat.get_prize())
            else:
                prize1 = prize1 + Meat.get_prize()
        if("Onions" in last_selected1_sauces[i]):
            if(["Onions", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Onions.get_prize())
            else:
                prize1 = prize1 + Onions.get_prize()
        if("Corn" in last_selected1_sauces[i]):
            if(["Corn", True] == last_selected1_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Corn.get_prize())
            else:
                prize1 = prize1 + Corn.get_prize()
        return prize1
    def sauce_prize2(i, prize1):
        if("Olives" in last_selected2_sauces[i]):
            if(["Olives", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Olives.get_prize())
            else:
                prize1 = prize1 + Olives.get_prize()
        if("Mushrooms" in last_selected2_sauces[i]):
            if(["Mushrooms", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Mushrooms.get_prize())
            else:
                prize1 = prize1 + Mushrooms.get_prize()
        if("GoatCheese" in last_selected2_sauces[i]):
            if(["GoatCheese", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * GoatCheese.get_prize())
            else:
                prize1 = prize1 + GoatCheese.get_prize()
        if("Meat" in last_selected2_sauces[i]):
            if(["Meat", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Meat.get_prize())
            else:
                prize1 = prize1 + Meat.get_prize()
        if("Onions" in last_selected2_sauces[i]):
            if(["Onions", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Onions.get_prize())
            else:
                prize1 = prize1 + Onions.get_prize()
        if("Corn" in last_selected2_sauces[i]):
            if(["Corn", True] == last_selected2_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Corn.get_prize())
            else:
                prize1 = prize1 + Corn.get_prize()
        return prize1
    def sauce_prize3(i, prize1):
        if("Olives" in last_selected3_sauces[i]):
            if(["Olives", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Olives.get_prize())
            else:
                prize1 = prize1 + Olives.get_prize()
        if("Mushrooms" in last_selected3_sauces[i]):
            if(["Mushrooms", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Mushrooms.get_prize())
            else:
                prize1 = prize1 + Mushrooms.get_prize()
        if("GoatCheese" in last_selected3_sauces[i]):
            if(["GoatCheese", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * GoatCheese.get_prize())
            else:
                prize1 = prize1 + GoatCheese.get_prize()
        if("Meat" in last_selected3_sauces[i]):
            if(["Meat", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Meat.get_prize())
            else:
                prize1 = prize1 + Meat.get_prize()
        if("Onions" in last_selected3_sauces[i]):
            if(["Onions", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Onions.get_prize())
            else:
                prize1 = prize1 + Onions.get_prize()
        if("Corn" in last_selected3_sauces[i]):
            if(["Corn", True] == last_selected3_sauces_and_extra[i]):
                prize1 = prize1 + (1.5 * Corn.get_prize())
            else:
                prize1 = prize1 + Corn.get_prize()
        return prize1


    last_selected0_sauces = []
    last_selected1_sauces = []
    last_selected2_sauces = []
    last_selected3_sauces = []
    last_selected00_sauces = []
    last_selected11_sauces = []
    last_selected22_sauces = []
    last_selected33_sauces = []
    last_selected_extra = []
    total_prize00 = []
    total_prize11 = []
    total_prize22 = []
    total_prize33 = []
    last_selected0_sauces_and_extra = []
    last_selected1_sauces_and_extra = []
    last_selected2_sauces_and_extra = []
    last_selected3_sauces_and_extra = []
    def a(j):
        prize1 = 0
        for i in range(last_selected0[j].__len__() - 2):
            last_selected0_sauces.append(last_selected0[j][i+2][0])
            last_selected_extra.append([last_selected0[j][i+2][1]])
            last_selected0_sauces_and_extra.append([last_selected0[j][i+2][0], last_selected0[j][i+2][1]])
            prize = sauce_prize0(i, prize1)
            prize1 = prize
        if(prize1 == 0):
            prize = 0
        temp = last_selected0_sauces
        last_selected00_sauces.append(temp)
        if(last_selected0[j][0] == "Classic"):
            print(str(last_selected0[j][1]) + " " + last_selected0[j][0] + " pizza incule: " + str(last_selected00_sauces[j]) + " and the prize is " + str((classic.get_prize(Classic) + prize) * last_selected0[j][1]) + " TL.")
            total_prize00.append((classic.get_prize(Classic) + prize) * last_selected0[j][1])
        if(last_selected0[j][0] == "Margherita"):
            print(str(last_selected0[j][1]) + " " + last_selected0[j][0] + " pizza incule: " + str(last_selected00_sauces[j]) + " and the prize is " + str((margherita.get_prize(Margherita) + prize) * last_selected0[j][1]) + " TL.")
            total_prize00.append((margherita.get_prize(Margherita) + prize) * last_selected0[j][1])
        if(last_selected0[j][0] == "TurkPizza"):
            print(str(last_selected0[j][1]) + " " + last_selected0[j][0] + " pizza incule: " + str(last_selected00_sauces[j]) + " and the prize is " + str((turkpizza.get_prize(TurkPizza) + prize) * last_selected0[j][1]) + " TL.")
            total_prize00.append((turkpizza.get_prize(TurkPizza) + prize) * last_selected0[j][1])
        if(last_selected0[j][0] == "PlainPizza"):
            print(str(last_selected0[j][1]) + " " + last_selected0[j][0] + " pizza incule: " + str(last_selected00_sauces[j]) + " and the prize is " + str((plainpizza.get_prize(PlainPizza) + prize) * last_selected0[j][1]) + " TL.")
            total_prize00.append((plainpizza.get_prize(PlainPizza) + prize) * last_selected0[j][1])
        temp.clear()
    def b(j):
        prize1 = 0
        for i in range(last_selected1[j].__len__() - 2):
            last_selected1_sauces.append(last_selected1[j][i+2][0])
            last_selected_extra.append([last_selected1[j][i+2][1]])
            last_selected1_sauces_and_extra.append([last_selected1[j][i+2][0], last_selected1[j][i+2][1]])
            prize = sauce_prize1(i, prize1)
            prize1 = prize
        if(prize1 == 0):
            prize = 0
        temp = last_selected1_sauces
        last_selected11_sauces.append(temp)
        if(last_selected1[j][0] == "Classic"):
            print(str(last_selected1[j][1]) + " " + last_selected1[j][0] + " pizza incule: " + str(last_selected11_sauces[j]) + " and the prize is " + str((classic.get_prize(Classic) + prize) * last_selected1[j][1]) + " TL.")
            total_prize11.append((classic.get_prize(Classic) + prize) * last_selected1[j][1])
        if(last_selected1[j][0] == "Margherita"):
            print(str(last_selected1[j][1]) + " " + last_selected1[j][0] + " pizza incule: " + str(last_selected11_sauces[j]) + " and the prize is " + str((margherita.get_prize(Margherita) + prize) * last_selected1[j][1]) + " TL.")
            total_prize11.append((margherita.get_prize(Margherita) + prize) * last_selected1[j][1])
        if(last_selected1[j][0] == "TurkPizza"):
            print(str(last_selected1[j][1]) + " " + last_selected1[j][0] + " pizza incule: " + str(last_selected11_sauces[j]) + " and the prize is " + str((turkpizza.get_prize(TurkPizza) + prize) * last_selected1[j][1]) + " TL.")
            total_prize11.append((turkpizza.get_prize(TurkPizza) + prize) * last_selected1[j][1])
        if(last_selected1[j][0] == "PlainPizza"):
            print(str(last_selected1[j][1]) + " " + last_selected1[j][0] + " pizza incule: " + str(last_selected11_sauces[j]) + " and the prize is " + str((plainpizza.get_prize(PlainPizza) + prize) * last_selected1[j][1]) + " TL.")
            total_prize11.append((plainpizza.get_prize(PlainPizza) + prize) * last_selected1[j][1])
        temp.clear()
    def c(j):
        prize1 = 0
        for i in range(last_selected2[j].__len__() - 2):
            last_selected2_sauces.append(last_selected2[j][i+2][0])
            last_selected_extra.append([last_selected2[j][i+2][1]])
            last_selected2_sauces_and_extra.append([last_selected2[j][i+2][0], last_selected2[j][i+2][1]])
            prize = sauce_prize2(i, prize1)
            prize1 = prize
        if(prize1 == 0):
            prize = 0
        temp = last_selected2_sauces
        last_selected22_sauces.append(temp)
        if(last_selected2[j][0] == "Classic"):
            print(str(last_selected2[j][1]) + " " + last_selected2[j][0] + " pizza incule: " + str(last_selected22_sauces[j]) + " and the prize is " + str((classic.get_prize(Classic) + prize) * last_selected2[j][1]) + " TL.")
            total_prize22.append((classic.get_prize(Classic) + prize) * last_selected2[j][1])
        if(last_selected2[j][0] == "Margherita"):
            print(str(last_selected2[j][1]) + " " + last_selected2[j][0] + " pizza incule: " + str(last_selected22_sauces[j]) + " and the prize is " + str((margherita.get_prize(Margherita) + prize) * last_selected2[j][1]) + " TL.")
            total_prize22.append((margherita.get_prize(Margherita) + prize) * last_selected2[j][1])
        if(last_selected2[j][0] == "TurkPizza"):
            print(str(last_selected2[j][1]) + " " + last_selected2[j][0] + " pizza incule: " + str(last_selected22_sauces[j]) + " and the prize is " + str((turkpizza.get_prize(TurkPizza) + prize) * last_selected2[j][1]) + " TL.")
            total_prize22.append((turkpizza.get_prize(TurkPizza) + prize) * last_selected2[j][1])
        if(last_selected2[j][0] == "PlainPizza"):
            print(str(last_selected2[j][1]) + " " + last_selected2[j][0] + " pizza incule: " + str(last_selected22_sauces[j]) + " and the prize is " + str((plainpizza.get_prize(PlainPizza) + prize) * last_selected2[j][1]) + " TL.")
            total_prize22.append((plainpizza.get_prize(PlainPizza) + prize) * last_selected2[j][1])
        temp.clear()
    def d(j):
        prize1 = 0
        for i in range(last_selected3[j].__len__() - 2):
            last_selected3_sauces.append(last_selected3[j][i+2][0])
            last_selected_extra.append([last_selected3[j][i+2][1]])
            last_selected3_sauces_and_extra.append([last_selected3[j][i+2][0], last_selected3[j][i+2][1]])
            prize = sauce_prize3(i, prize1)
            prize1 = prize
        if(prize1 == 0):
            prize = 0
        temp = last_selected3_sauces
        last_selected33_sauces.append(temp)
        if(last_selected3[j][0] == "Classic"):
            print(str(last_selected3[j][1]) + " " + last_selected3[j][0] + " pizza incule: " + str(last_selected33_sauces[j]) + " and the prize is " + str((classic.get_prize(Classic) + prize) * last_selected3[j][1]) + " TL.")
            total_prize33.append((classic.get_prize(Classic) + prize) * last_selected3[j][1])
        if(last_selected3[j][0] == "Margherita"):
            print(str(last_selected3[j][1]) + " " + last_selected3[j][0] + " pizza incule: " + str(last_selected33_sauces[j]) + " and the prize is " + str((margherita.get_prize(Margherita) + prize) * last_selected3[j][1]) + " TL.")
            total_prize33.append((margherita.get_prize(Margherita) + prize) * last_selected3[j][1])
        if(last_selected3[j][0] == "TurkPizza"):
            print(str(last_selected3[j][1]) + " " + last_selected3[j][0] + " pizza incule: " + str(last_selected33_sauces[j]) + " and the prize is " + str((turkpizza.get_prize(TurkPizza) + prize) * last_selected3[j][1]) + " TL.")
            total_prize33.append((turkpizza.get_prize(TurkPizza) + prize) * last_selected3[j][1])
        if(last_selected3[j][0] == "PlainPizza"):
            print(str(last_selected3[j][1]) + " " + last_selected3[j][0] + " pizza incule: " + str(last_selected33_sauces[j]) + " and the prize is " + str((plainpizza.get_prize(PlainPizza) + prize) * last_selected3[j][1]) + " TL.")
            total_prize33.append((plainpizza.get_prize(PlainPizza) + prize) * last_selected3[j][1])
        temp.clear()


    def payment_decide():
        for j in range(last_selected0.__len__()):
            a(j)
        if(last_selected1.__len__() == 0):
            pass
        else:
            for j in range(last_selected1.__len__()):
                b(j)
            if(last_selected2.__len__() == 0):
                pass
            else:
                for j in range(last_selected2.__len__()):
                    c(j)
                if(last_selected3.__len__() == 0):
                    pass
                else:
                    for j in range(last_selected3.__len__()):
                        d(j)


    def payment_info(total_prize):
        print("")
        print("You gonna pay " + str(total_prize) + " TL.")
        name = input("Please enter your name: ")
        x = 0
        while(x == 0):
            try:
                number = int(input("Please enter your ID number: "))
            except Exception:
                print("You entered invalid value!")
            else:
                number1 = str(number)
                if(number1.__len__() == 11):
                    ID_number = number
                    x = 1
                else:
                    print("You must enter 11 digits!")
        y = 0
        while(y == 0):
            try:
                number = int(input("Please enter your credit card number: "))
            except Exception:
                print("You entered invalid value!")
            else:
                number1 = str(number)
                if(number1.__len__() == 16):
                    credit_card_number = number
                    y = 1
                else:
                    print("You must enter 16 digits!")
        z = 0
        while(z == 0):
            try:
                number = int(input("Please enter your credit card password: "))
            except Exception:
                print("You entered invalid value!")
            else:
                number1 = str(number)
                if(number1.__len__() == 4):
                    credit_card_password = number
                    z = 1
                else:
                    print("You must enter 4 digits!")
        time1 = datetime.now()
        time2 = time1.strftime("%d/%m/%Y %H:%M:%S")
        payment_info_file = [name, ID_number, credit_card_number, credit_card_password, time2]
        print(name + " pay " + str(total_prize) + " TL with the card and card number is " + str(credit_card_number) + ". And the date was " + str(time2))
        with open("Orders_Database.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Numbers", "Type of Pizzas", "Type of Sauces and Extras", "Prizes"])
            total_prize = 0
            for i in range(total_prize00.__len__()):
                total_prize = total_prize + total_prize00[i]
            for i in range(total_prize11.__len__()):
                total_prize = total_prize + total_prize11[i]
            for i in range(total_prize22.__len__()):
                total_prize = total_prize + total_prize22[i]
            for i in range(total_prize33.__len__()):
                total_prize = total_prize + total_prize33[i]
            for i in range(last_selected0.__len__()):
                for j in range(last_selected0[i].__len__()):
                    if(j > 1):
                        if(last_selected0[i][j][1] == True):
                            info0.append(f"{last_selected0[i][j][0]} (Extra)")
                        else:
                            info0.append(last_selected0[i][j][0])
                    else:
                        info.append(last_selected0[i][j])
                info.append(f"{info0}")
                info.append(total_prize00[i])
                info_general.append(info)
                writer.writerow(info)
                info0.clear()
                info.clear()
            for i in range(last_selected1.__len__()):
                for j in range(last_selected1[i].__len__()):
                    if(j > 1):
                        if(last_selected1[i][j][1] == True):
                            info1.append(f"{last_selected1[i][j][0]} (Extra)")
                        else:
                            info1.append(last_selected1[i][j][0])
                    else:
                        info.append(last_selected1[i][j])
                info.append(f"{info1}")
                info.append(total_prize11[i])
                info_general.append(info)
                writer.writerow(info)
                info1.clear()
                info.clear()
            for i in range(last_selected2.__len__()):
                for j in range(last_selected2[i].__len__()):
                    if(j > 1):
                        if(last_selected2[i][j][1] == True):
                            info2.append(f"{last_selected2[i][j][0]} (Extra)")
                        else:
                            info2.append(last_selected2[i][j][0])
                    else:
                        info.append(last_selected2[i][j])
                info.append(f"{info2}")
                info.append(total_prize22[i])
                info_general.append(info)
                writer.writerow(info)
                info2.clear()
                info.clear()
            for i in range(last_selected3.__len__()):
                for j in range(last_selected3[i].__len__()):
                    if(j > 1):
                        if(last_selected3[i][j][1] == True):
                            info3.append(f"{last_selected3[i][j][0]} (Extra)")
                        else:
                            info3.append(last_selected3[i][j][0])
                    else:
                        info.append(last_selected3[i][j])
                info.append(f"{info3}")
                info.append(total_prize33[i])
                info_general.append(info)
                writer.writerow(info)
                info3.clear()
                info.clear()
            writer.writerow("")
            writer.writerow(["Name", "ID_number", "Credit Card Number", "Credit Card Password", "Date"])
            writer.writerow(payment_info_file)
        file.close()
        print("Enjoy your Meal!")


    def payment_cancel():
        ans = input("Do you want to leave or change pizzas? (leave/change): ").lower()
        match(ans):
            case "leave":
                print("Goodbye!")
            case "change":
                print("")
                if __name__ == "__main__":
                    main()
            case _:
                print("Invalid input!")
                payment_cancel()


    def payment_ask(total_prize):
        ans = input("Do you want to continue or cancel? (continue/cancel): ").lower()
        match(ans):
            case "continue":
                payment_info(total_prize)
            case "cancel":
                payment_cancel()
            case _:
                print("Invalid input!")
                payment_ask(total_prize)


    info_general = []
    info = []
    info0 = []
    info1 = []
    info2 = []
    info3 = []
    def payment():
        print("")
        print("Here is the slip:")
        with open("Orders_Database.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Numbers", "Type of Pizzas", "Type of Sauces and Extras", "Prizes"])
            total_prize = 0
            for i in range(total_prize00.__len__()):
                total_prize = total_prize + total_prize00[i]
            for i in range(total_prize11.__len__()):
                total_prize = total_prize + total_prize11[i]
            for i in range(total_prize22.__len__()):
                total_prize = total_prize + total_prize22[i]
            for i in range(total_prize33.__len__()):
                total_prize = total_prize + total_prize33[i]
            for i in range(last_selected0.__len__()):
                for j in range(last_selected0[i].__len__()):
                    if(j > 1):
                        if(last_selected0[i][j][1] == True):
                            info0.append(f"{last_selected0[i][j][0]} (Extra)")
                        else:
                            info0.append(last_selected0[i][j][0])
                    else:
                        info.append(last_selected0[i][j])
                info.append(f"{info0}")
                info.append(total_prize00[i])
                info_general.append(info)
                writer.writerow(info)
                info0.clear()
                info.clear()
            for i in range(last_selected1.__len__()):
                for j in range(last_selected1[i].__len__()):
                    if(j > 1):
                        if(last_selected1[i][j][1] == True):
                            info1.append(f"{last_selected1[i][j][0]} (Extra)")
                        else:
                            info1.append(last_selected1[i][j][0])
                    else:
                        info.append(last_selected1[i][j])
                info.append(f"{info1}")
                info.append(total_prize11[i])
                info_general.append(info)
                writer.writerow(info)
                info1.clear()
                info.clear()
            for i in range(last_selected2.__len__()):
                for j in range(last_selected2[i].__len__()):
                    if(j > 1):
                        if(last_selected2[i][j][1] == True):
                            info2.append(f"{last_selected2[i][j][0]} (Extra)")
                        else:
                            info2.append(last_selected2[i][j][0])
                    else:
                        info.append(last_selected2[i][j])
                info.append(f"{info2}")
                info.append(total_prize22[i])
                info_general.append(info)
                writer.writerow(info)
                info2.clear()
                info.clear()
            for i in range(last_selected3.__len__()):
                for j in range(last_selected3[i].__len__()):
                    if(j > 1):
                        if(last_selected3[i][j][1] == True):
                            info3.append(f"{last_selected3[i][j][0]} (Extra)")
                        else:
                            info3.append(last_selected3[i][j][0])
                    else:
                        info.append(last_selected3[i][j])
                info.append(f"{info3}")
                info.append(total_prize33[i])
                info_general.append(info)
                writer.writerow(info)
                info3.clear()
                info.clear()
        with open("Orders_Database.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        payment_ask(total_prize)


    def payment_before():
        print("")
        payment_decide()
        payment()


    def answer():
        ans = input("Do you want to information of the menu? (y/n): ")
        match(ans):
            case "y":
                print("")
                classic.get_info(Classic)
                margherita.get_info(Margherita)
                turkpizza.get_info(TurkPizza)
                plainpizza.get_info(PlainPizza)
                sauce_type.get_info(Olives)
                sauce_type.get_info(Mushrooms)
                sauce_type.get_info(GoatCheese)
                sauce_type.get_info(Meat)
                sauce_type.get_info(Onions)
                sauce_type.get_info(Corn)
                i = 1
                return 1
            case "n":
                return 1
            case _:
                print("Invalid input!")
                answer()



    print("Welcome to Pizza")
    print("Here is the menu:")
    print("\nType of Pizza:" + "\t\tType of Sauce:")
    for i in range(6):
        if i<4:
            print(menu_pizza_types[i] + "\t\t" + menu_pizza_sauce[i])
        else:
            print("\t\t\t" + menu_pizza_sauce[i])
    print("")


    Classic = classic("Classic", 20.0)
    Margherita = margherita("Margherita", 30.0)
    TurkPizza = turkpizza("TurkPizza", 35.0)
    PlainPizza = plainpizza("PlainPizza", 15.0)
    Olives = sauce_type("Olives", 0.5)
    Mushrooms = sauce_type("Mushrooms", 1.0)
    GoatCheese = sauce_type("GoatCheese", 3.0)
    Meat = sauce_type("Meat", 5.0)
    Onions = sauce_type("Onions", 0.75)
    Corn = sauce_type("Corn", 0.25)
    answer()
    print("")


    last_selected = [["", 0],["", 0],["", 0],["", 0]]
    last_selected0 = []
    last_selected1 = []
    last_selected2 = []
    last_selected3 = []
    bb = []


    aa = 0
    selected0 = select_pizza()
    while(selected0 == bb):
        print("You have to buy at least one pizza!")
        selected0 = select_pizza()
    last_selected[aa] = selected0
    select_sauce_q(aa)
    if(last_selected[aa][1] != 0):
        last_selected0.append(last_selected[aa])


    print("")
    print("For the other pizzas:")
    aa = 1
    selected1 = select_pizza()
    if(selected1 == bb):
        payment_before()
    else:
        last_selected[aa] = selected1
        select_sauce_q(aa)
        if(last_selected[aa][1] != 0):
            last_selected1.append(last_selected[aa])


        print("")
        print("For the other pizzas:")
        aa = 2
        selected2 = select_pizza()
        if(selected2 == bb):
            payment_before()
        else:
            last_selected[aa] = selected2
            select_sauce_q(aa)
            if(last_selected[aa][1] != 0):
                last_selected2.append(last_selected[aa])


            print("")
            print("For the other pizzas:")
            aa = 3
            selected3 = select_pizza()
            if(selected3 == bb):
                payment_before()
            else:
                last_selected[aa] = selected3
                select_sauce_q(aa)
                if(last_selected[aa][1] != 0):
                    last_selected3.append(last_selected[aa])
                payment_before()



if __name__ == "__main__":
    main()
