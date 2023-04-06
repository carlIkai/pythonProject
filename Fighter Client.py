
# Import fighter class
from Fighter import *

def main() -> None:
    # Commit
    # Annotate variables
    #color = Fighter()
    #name = Fighter()
    #stats = Fighter()
    #strengths = Fighter()
    name_1: str = "carl"
    color_1: str = "blue"
    stats_1: int = 13
    my_list_1: list = "wise", "chill"
    name_2: str = "Seiji"
    color_2: str = "green"
    stats_2: int = 69
    my_list_2: list = "dope", "sexy", "suave"
    name_3: str = "bunu"
    color_3: str = "purple"
    stats_3: int = 26
    my_list_3: list = "robust", "insatiable", "intimate"

    F1 = Fighter(name_1, color_1, stats_1, my_list_1)
    F2 = Fighter(name_2, color_2, stats_2, my_list_2)
    F3 = Fighter(name_3, color_3, stats_3, my_list_3)

    print("Fighter 1")
    F1.introduce_self()
    print("Fighter 2")
    F2.introduce_self()
    print("Fighter 3")
    F3.introduce_self()

    F2.add_name("Thomaso")
    print("Fighter 2")
    F2.introduce_self()
    #name.add_name("Johnny")
    #color.add_color("blue")
    #stats.add_stats(13)
    #strengths.add_strengths("strong")
    #strengths.add_strengths("wise")
    #strengths.add_strengths("chill")


    #print("Name: " + str(name.add_name("Johnny")))
    #print("Stats: " + str(stats.add_stats(13)))

main()
