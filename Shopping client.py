
from ShoppingList import *

def main() -> None:

    # Create shopping list
    my_list = ShoppingList()
    my_list.add_item("milk")
    my_list.add_item("bread")
    my_list.add_item("peanut butter")

    # Show list and all items in the list
    print("List: " + str(my_list.get_list()))
    print("All items: " + str(my_list.get_all_items()))

    # remove and add items to the list
    my_list.remove_item("bread")
    my_list.add_item("pickles")
    my_list.add_item("seracha")

    # Show items on the list
    print("List: " + str(my_list.get_list()))
    print("All items: " + str(my_list.get_list()))

main()






