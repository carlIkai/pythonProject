from BudsClass import *

def main() -> None:

    k_b: dict

    my_bud_association1 = BudsClass("Blue dream", 30.2)
    my_bud_association2 = BudsClass("Gorilla glue", 20.2)
    my_bud_association3 = BudsClass("Haze", 30.5)
    my_bud_association4 = BudsClass("Pineapple", 20.7)

    k_b = {
        "Novel": " pride",
        "Author": "Chiller",
        "year": "1982"
    }

    k_b["Author"] = "James Joyce"

    print(k_b.keys())
    print(k_b.values())
    my_bud_association1.print_object()
    my_bud_association2.print_object()
    my_bud_association3.print_object()
    my_bud_association4.print_object()

main()
