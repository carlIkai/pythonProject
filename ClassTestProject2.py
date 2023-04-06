class NegativePriceError(Exception):
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
            raise NegativePriceError

        if selling_price >= 0:
            self._selling_price = selling_price
        else:
            raise NegativePriceError


    def get_name(self) -> str:
        """Method to retrieve menu item name."""
        return self._item_name

    def get_wholesale_cost(self) -> float:
        """Method to retrieve menu item wholesale cost."""
        return self._wholesale_cost

    def get_selling_price(self) -> float:
        """Method to retrieve menu item selling price"""
        return self._selling_price




