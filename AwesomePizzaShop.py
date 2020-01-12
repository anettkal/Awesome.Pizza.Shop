class PizzaShop:

    def __init__(self, name, address, opening_time):
        self.name = name
        self.address = address
        self.opening_time = opening_time

    def choose_next_option(self):
        print("Welcome!")
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
                print("Do you want to view pizza selection" +
                      " or make own AWESOME pizza?")
                select = input("Press 1, for pizza selection, press 2," +
                               "to make own Awesome pizza.\n")
                if select == '1':
                    pizza_list = self.build_pizza()
                    for pizza in pizza_list:
                        print(pizza.to_string())
            elif option == '3':
                print("Goodbye! See you next time.")
                break
            else:
                self.choose_next_option()

    def build_pizza(self):
        pizza_margherita = MargheritaPizza()
        pizza_mushroom = MushroomPizza()
        pizza_four_cheese = FourCheesePizza()
        pizza_ham_mushroom = HamMushroomPizza()
        pizza_seafood = SeafoodPizza()
        pizza_list = []
        pizza_list.append(pizza_margherita)
        pizza_list.append(pizza_mushroom)
        pizza_list.append(pizza_four_cheese)
        pizza_list.append(pizza_ham_mushroom)
        pizza_list.append(pizza_seafood)
        return pizza_list


class Pizza:
    def __init__(self, name, list_of_ingredients, price):
        self.name = name
        self.price = price
        self.list_of_ingredients = list_of_ingredients

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.list_of_ingredients

    def to_string(self):
        return "Name: " + str(self.name) + " Ingredients: " \
               + str(self.list_of_ingredients) + " Price(€): " \
               + str(self.price)


class MargheritaPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Margarita", "tomato sauce, cheese", 7)


class MushroomPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Funghi", "tomato sauce," +
                       "cheese, mushrooms", 9)


class FourCheesePizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Quattro Formaggi", "emmental," +
                       "mozzarella, gorgonzola, parmigiano", 12)


class HamMushroomPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Prosciutto e Funghi",
                       "tomato sauce, mushrooms, ham, cheese", 10)


class SeafoodPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Frutti di Mare", "tomato sauce," +
                       "clams, mussels, prawns", 13)


if __name__ == '__main__':
    ps = PizzaShop("Awesome PizzaShop, ", "Corso di Porta Romana 83," +
                   " 20122 Milano, ", "Monday - Saturday ~ (11:00 - 23:00), " +
                   "Sunday ~ (closed)")
    ps.choose_next_option()
