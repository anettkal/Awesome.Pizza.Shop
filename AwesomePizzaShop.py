class PizzaShop:

    def __init__(self, name, address, opening_time):
        self.name = name
        self.address = address
        self.opening_time = opening_time

    def choose_next_option(self):
        print("Welcome!")
        while True:
            option = input("Menu\nChoose 1, 2, 3 for the following options:\n" +
                           "1) Display information of the shop (Name, address, Opening / closing Time)\n" +
                           "2) Order Pizza\n" +
                           "3) Exit\n")
            if option == '1':
                print(self.name + self.address + self.opening_time)
            elif option == '2':
                print("Do you want to view pizza selection or make own AWESOME pizza?")
                select = input("Press 1, for pizza selection, press 2, to make own Awesome pizza.")
            elif option == '3':
                print("Goodbye! See you next time.")
                break
            else:
                self.choose_next_option()


class Pizza:
    def __init__(self, name, list_of_ingredients, price):
        self.name = name
        self.price = price
        self.list_of_ingredients = list_of_ingredients

    def get_price(self):
        return self.price


if __name__ == '__main__':
    ps = PizzaShop("Awesome PizzaShop, ", "Corso di Porta Romana 83, 20122 Milano, ",
                   "Monday - Saturday ~ (11:00 - 23:00), Sunday ~ (closed)")
    ps.choose_next_option()

