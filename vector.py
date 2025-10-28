class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conections = []

    def get_length_qrt(self):
        return self.x ** 2 + self.y ** 2

    def get_length(self):
        return self.get_length_qrt() ** 0.5
    
    def conect(self, vector:"Vector2D"):
        self.conections.append(vector)

class Vector3D:
    len_diagonal = 2 ** 0.5
    z_vector = Vector2D(-len_diagonal, len_diagonal)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.conections = []

    def get_length_qrt(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def get_length(self):
        return self.get_length_qrt() ** 0.5
    
    def convert_to_2d(self, pos):
        return Vector2D(self.x + pos[3].x + Vector3D.z_vector.x * (self.z + pos[3].z), self.y + pos[3].y + Vector3D.z_vector.y * (self.z + pos[3].z))

    def conect(self, vector:"Vector3D"):
        self.conections.append(vector)