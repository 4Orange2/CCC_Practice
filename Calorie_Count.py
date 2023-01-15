def burger_cal(choice_num):
    calories = 0
    if choice_num == "1":
        calories = 461
    elif choice_num == "2":
        calories = 431
    elif choice_num == "3":
        calories = 420
    elif choice_num == "4":
        pass
    return calories

def drink_cal(choice_num):
    calories = 0
    if choice_num == "1":
        calories = 130
    elif choice_num == "2":
        calories = 160
    elif choice_num == "3":
        calories = 118
    elif choice_num == "4":
        pass
    return calories

def side_cal(choice_num):
    calories = 0
    if choice_num == "1":
        calories = 100
    elif choice_num == "2":
        calories = 57
    elif choice_num == "3":
        calories = 70
    elif choice_num == "4":
        pass
    return calories

def dessert_cal(choice_num):
    calories = 0
    if choice_num == 1:
        calories = 167
    elif choice_num == 2:
        calories = 266
    elif choice_num == 3:
        calories = 75
    elif choice_num == 4:
        pass
    return calories

def calorie_count():
    print("You have three burger choices \n"
          "1 - Cheeseburger \n"
          "2 - Fish Burger \n"
          "3 - Veggie Burger \n"
          "4- no burger \n")
    print("You have three drink choices \n"
          "1 - Soft Drink \n"
          "2 - Orange Juice \n"
          "3 - Milk \n"
          "4- no drink \n")
    print("You have three side order choices \n"
          "1 - Fries \n"
          "2 - Baked Potato \n"
          "3 - Chef Salad \n"
          "4- no side order \n")
    print("You have three dessert choices \n"
          "1 - Apple Pie \n"
          "2 - Sundae \n"
          "3 - Fruit Cup \n"
          "4 - no dessert \n")
    burger = input("Burger Choice: ")
    drink = input("Drink Choice: ")
    side = input("Side Order Choice: ")
    dessert = input("Dessert Choice: ")
    calBurg = burger_cal(burger)
    calDrink = drink_cal(drink)
    calSide = side_cal(side)
    calDessert = dessert_cal(dessert)
    calories = calBurg + calDrink + calSide + calDessert
    return calories

print(calorie_count())