class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def _iter_(self):
        yield ('length', self.length)
        yield ('width', self.width)
rect = Rectangle(5, 3)
for key, value in rect:
    print(f'{key}: {value}')

