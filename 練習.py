class pen():
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(self.name, self.color, self.price)

        from types import BuiltinFunctionType


red_pen1 = pen("PARKER", "red", 10)  # 獨立的
blue_pen1 = pen("PARKER", "blue", 16)
red_pen2 = pen("LAMY", "red", 10)  # 獨立的

red_pen1 == red_pen2  # 屬性一樣 但兩個是獨立的

red_pen1.show()
blue_pen1.show()
red_pen2.show()
