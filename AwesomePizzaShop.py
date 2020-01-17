import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


class PizzaShop:

    def __init__(self, name, address, opening_time):
        self.name = name
        self.address = address
        self.opening_time = opening_time
        self.pizza_list = self.build_pizza()

    def choose_next_option(self):
        print("Welcome!")
        self.view_menu()

    def build_pizza(self):
        pizza_margherita = MargheritaPizza()
        pizza_mushroom = MushroomPizza()
        pizza_four_cheese = FourCheesePizza()
        pizza_ham_mushroom = HamMushroomPizza()
        pizza_seafood = SeafoodPizza()
        pizza_list = [pizza_margherita, pizza_mushroom,
                      pizza_four_cheese, pizza_ham_mushroom, pizza_seafood]
        return pizza_list

    def get_pizza(self, pizza_number):
        for pizza in self.pizza_list:
            if pizza_number == pizza.get_number():
                return pizza

    def view_menu(self):
        while True:
            option = input("Menu\n" +
                           "Choose 1, 2, 3 for the following options:\n" +
                           "1) Display information of the" +
                           "shop (Name, address," +
                           "Opening / closing Time)\n" +
                           "2) Order Pizza\n" +
                           "3) Exit\n")
            if option == '1':
                print(self.name + self.address + self.opening_time)
            elif option == '2':
                self.view_selection()
            elif option == '3':
                print("Goodbye! See you next time.")
                break
            else:
                self.choose_next_option()

    def view_selection(self):
        print("Do you want to view pizza selection" +
              " or make own AWESOME pizza?")
        select = input("Press 1) for pizza selection, press 2) " +
                       "to make own Awesome pizza.\n")
        if select == '1':
            for pizza in self.pizza_list:
                print(pizza.to_string())
            self.add_to_cart()
        elif select == '2':
            pass
        else:
            self.view_selection()

    def add_to_cart(self):
        cart = []
        pizza_selection_number = input("\nWhich pizza do you want" +
                                       " to add to Cart?\n" +
                                       "Please select the " +
                                       "corresponding number!\n")
        if '1' <= pizza_selection_number <= '5':
            pizza = self.get_pizza(pizza_selection_number)
            print(str(pizza.get_name()), str(pizza.get_price()))
            cart.append(pizza)
        else:
            self.add_to_cart()
        while True:
            cart_status = input("\nYour cart is not empty," +
                                "do you want to remove items?\n" +
                                "~To remove all items press 1)\n" +
                                "~To go to pay press 2)\n" +
                                "~To go back to Pizza-shop " +
                                "Menu press 0)\n")
            if cart_status == "1":
                del cart[:]
                print("You successfully removed all items from the list")
                self.view_menu()
                break
            elif cart_status == "2":
                print(pizza.get_name(), pizza.get_price())
                self.making_pizzas()
                break
            elif cart_status == "0":
                self.view_menu()
                break

    def making_pizzas(self):
        make_pizza = input("Please press 1) to pay and " +
                           "we start to make your pizza " +
                           "press 2 to go back Main Menu")
        if make_pizza == "1":
            print_pause("Preparing the pasta...")
            print_pause("Putting on the ingredients...")
            print_pause("Pizza is in the oven...")
            print_pause("3")
            print_pause("2")
            print_pause("1")
            print_pause("Pizza is ready. Enjoy!\n")
        elif make_pizza == "2":
            self.view_menu()
        else:
            self.making_pizzas()


class Pizza:
    def __init__(self, number, name, list_of_ingredients, price):
        self.name = name
        self.price = price
        self.list_of_ingredients = list_of_ingredients
        self.number = number

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.list_of_ingredients

    def get_number(self):
        return self.number

    def to_string(self):
        return str(self.number) + " Name: " \
               + str(self.name) + " Ingredients: " \
               + str(self.list_of_ingredients) + " Price(€): " \
               + str(self.price)


class MargheritaPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "1", "Pizza Margarita", "tomato sauce, cheese", 7)


class MushroomPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "2", "Pizza Funghi", "tomato sauce," +
                       "cheese, mushrooms", 9)


class FourCheesePizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "3", "Pizza Quattro Formaggi", "emmental," +
                       "mozzarella, gorgonzola, parmigiano", 12)


class HamMushroomPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "4", "Pizza Prosciutto e Funghi",
                       "tomato sauce, mushrooms, ham, cheese", 10)


class SeafoodPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "5", "Pizza Frutti di Mare", "tomato sauce," +
                       "clams, mussels, prawns", 13)


if __name__ == '__main__':
    ps = PizzaShop("Awesome PizzaShop, ", "Corso di Porta Romana 83," +
                   " 20122 Milano, ", "Monday - Saturday ~ (11:00 - 23:00), " +
                   "Sunday ~ (closed)")
    ps.choose_next_option()
