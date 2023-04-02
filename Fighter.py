
class Fighter():

    # Annotate variables
    _name = str
    _color = str
    _stats = int
    _strengths = list

    def __init__(self, name: str, color: str, stats: int, strengths: list) -> None:
        self._name = name
        self._color = color
        self._stats = stats
        self._strengths = strengths

    def introduce_self(self):
        print("Name: " + self._name)
        print("Color: " + self._color)
        print("Stats: " + str(self._stats))
        print("Attributes: " + str(self._strengths))

    def add_name(self, name: str) -> str:
        self._name = name
        return name

    def add_color(self, color: str) -> str:
        return self._color(color)

    def add_stats(self, stats: int) -> int:
        return self._stats(stats)

    def add_strengths(self, strength: str) -> list:
        return self._strengths(strength)







