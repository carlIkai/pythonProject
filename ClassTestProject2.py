class NegativeInputError(Exception):
    pass

class MenuItem:
    """MenuItem class is used to create and manage a menu item for a lemonade stand"""

    # Annotate variables.
    _item_name: str
    _wholesale_cost: float
    _selling_price: float

    def __init__(self, name: str, wholesale_cost: float, selling_price: float) -> None:
        self._item_name = name
        if wholesale_cost >= 0:
            self._wholesale_cost = wholesale_cost
        else:
            raise NegativeInputError

        if selling_price >= 0:
            self._selling_price = selling_price
        else:
            raise NegativeInputError


    def get_name(self) -> str:
        """Method to retrieve menu item name."""
        return self._item_name

    def get_wholesale_cost(self) -> float:
        """Method to retrieve menu item wholesale cost."""
        return self._wholesale_cost

    def get_selling_price(self) -> float:
        """Method to retrieve menu item selling price"""
        return self._selling_price

class SalesForDay:
    """Class that represents sales for a particular day"""

    # Annotate variables.
    _days_open: int
    _item_log: dict

    def __init__(self, num_of_days: int, sales_log: dict):
        if num_of_days >= 0:
            self._days_open = num_of_days
        else:
            raise NegativeInputError

        self._item_log = sales_log

    def get_day(self) -> int:
        """Method to retrieve day number for sales inventory."""
        return self._days_open

    def get_sales_dict(self) -> dict:
        """Method to retrieve sales for day dictionary."""
        return self._item_log

class LemonadeStand:
    """Class to construct and manage Lemon Stand objects"""
    # Annotate variables.
    _stand_name: str
    _current_day: int
    _menu_item_dict: dict
    _sales_for_day_log: list

    def __init__(self, name: str) -> None:
        self._stand_name = name
        self._current_day = 0
        self._menu_item_dict = {}
        self._sales_for_day_log = []

    def get_name(self) -> str:
        """Method to retrieve lemonade stand name"""
        return self._stand_name

    def add_menu_item(self, menu) -> None:
        """Method to add menu item to dictionary of menu items."""
        self._menu_item_dict.update({menu.get_name(): menu})

    def print_sales_for_day(self) -> None:
        """Test method to print out created dictionaries and lists."""
        print(self._sales_for_day_log)

    def enter_sales_for_today(self, sale_item: dict) -> None:
        """Method takes a dictionary of daily sales, and confirms that all items in the dictionary
        match corresponding items in the menu item dictionary. If all items match, an object
        of sales for day is created containing the current day, and the dictionary of daily sales."""
        test: bool = True
        for key in sale_item:
            if not key in self._menu_item_dict:
                test = False
        if test == True:
            day_sales = SalesForDay(self._current_day, sale_item)
            self._sales_for_day_log.append(day_sales)
            self._current_day += 1
            print(day_sales.get_day())
            print(day_sales.get_sales_dict())
        else:
            print("InvalidSalesItemError")


    def sales_of_menu_item_for_day(self, day_num: int, menu_item: str) -> int:
        """Method that takes a day value and item, and returns that item's sale amount for
        the given day."""
        for i in self._sales_for_day_log:
           if i.get_day() == day_num:
               day_menu = i.get_sales_dict()
               if menu_item in day_menu:
                  return(day_menu.get(menu_item))
            #for j in i:
                #if day_num == j:
                   #print(j.get_sales_dict())
                   #print(daily_sales)

                   #if menu_item in day_sales:
                       #print(day_sales.get(menu_item))

    def total_sales_for_menu_item(self, menu_item_name: str) -> int:
        """Method that takes a menu item, and returns the total sales for that menu item."""
        # Annotate variables
        total: int = 0
        for i in self._sales_for_day_log:
            item_amount = carl.sales_of_menu_item_for_day(i.get_day(), menu_item_name)
            total += item_amount
        return total

    def profit_for_menu_item(self, menu_item: str) -> float:
        """Method that takes a menu item, and returns that menu item's total profits."""
        if menu_item in self._menu_item_dict:
           val = self._menu_item_dict[menu_item]
           return((val.get_selling_price() - val.get_wholesale_cost()) * (carl.total_sales_for_menu_item(menu_item)))

    def total_profit_stand(self) -> float:
        """Method that calculates a lemonade stand's total profits."""
        keys_list = list(self._menu_item_dict.keys())
        print(keys_list)
        for i in keys_list:
            item = i
            #print(carl.profit_for_menu_item("Ricky"))




def main() -> None:
    sales: dict


sales1 = {
    "lemonade": 50,
    "Ricky Lime": 8,
    "Ricky T": 19,
    "soda": 9,
}
sales2 = {
    "Lim": 5,
    "Lime Ricky": 2,
    "Ricky": 5,
}
sales3 = {
    "Lime Ricky": 2,
    "Ricky": 5,
}
sales4 = {
    "Ricky": 5,
}
sales5 = {
    "Ricky": 5,
    "Lim": 19,
    "Lime Ricky": 9,
}
sales6 = {
    "Lime Ricky": 8,
    "Lim": 19,
    "Ricky": 5,
}

##sales1 = SalesForDay(20, sales)
##print(sales1.get_day())
##print(sales1.get_sales_dict())
menu1 = MenuItem("Lime Ricky", 2.50, 3.50)
menu2 = MenuItem("Lim", 2.50, 3.50)
menu3 = MenuItem("Ricky", 2.50, 4.50)

carl = LemonadeStand("carl")
carl.add_menu_item(menu1)
carl.add_menu_item(menu2)
carl.add_menu_item(menu3)

carl.enter_sales_for_today(sales1)
carl.enter_sales_for_today(sales2)
carl.enter_sales_for_today(sales3)
carl.enter_sales_for_today(sales4)
carl.enter_sales_for_today(sales5)
carl.enter_sales_for_today(sales6)
#carl.sales_of_menu_item_for_day(1, "lemonade")
carl.print_sales_for_day()
#carl.print_menu()
print(carl.total_sales_for_menu_item("Ricky"))
print(carl.profit_for_menu_item("Ricky"))
carl.total_profit_stand()
main()