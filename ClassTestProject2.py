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
        return self._days_open

    def get_sales_dict(self) -> dict:
        return self._item_log

class LemonadeStand:

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
        return self._stand_name

    def add_menu_item(self, menu: object) -> None:
        self._menu_item_dict.update({menu.get_name(): menu})



def main() -> None:
    sales: dict

sales = {
    "lemonade": 5,
    "cookie": 2
    }

##sales1 = SalesForDay(20, sales)
##print(sales1.get_day())
##print(sales1.get_sales_dict())
menu1 = MenuItem("Lime Ricky", 2.50, 3.50)

carl = LemonadeStand("carl")
print(carl.add_menu_item(menu1))

main()