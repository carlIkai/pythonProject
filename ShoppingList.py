
class ShoppingList():

    # Annotate Variables
    _items: list
    _all_items: list

    def __init__(self) -> None:
        self._items = []
        self._all_items = []

    def add_item(self, item: str) -> None:
        self._items.append(item)
        if not item in self._all_items:
            self._all_items.append(item)

    def remove_item(self, item: str) -> list:
        return self._items.remove(item)

    def get_list(self) -> list:
        return self._items.copy()

    def get_all_items(self) -> list:
        return self._all_items.copy()





