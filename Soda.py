class Soda:

    def __init__(self, taste):
        match taste:
            case "":
                self.taste = "обычная"
            case _:
                self.taste = taste

    def print_taste(self):
        if self.taste == "обычная":
            print("У вас обычная газировка")
        else:
            print(f"У вас газировка со вкусом <{self.taste}>")