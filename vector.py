class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length_qrt(self):
        return self.x ** 2 + self.y ** 2

    def get_length(self):
        return self.get_length_qrt() ** 0.5