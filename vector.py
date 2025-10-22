class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length_qrt(self):
        return self.x ** 2 + self.y ** 2

    def get_length(self):
        return self.get_length_qrt() ** 0.5

class Vector3D:
    len_diagonal = 2 ** 0.5
    z_vector = Vector2D(-len_diagonal, len_diagonal)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_length_qrt(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def get_length(self):
        return self.get_length_qrt() ** 0.5
    
    def convert_to_2d(self):
        return Vector2D(self.x + Vector3D.z_vector.x * self.z, self.y + Vector3D.z_vector.y * self.z)