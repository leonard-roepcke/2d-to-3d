import vector
from pygameApp import PygameApp
import random

class Main:
    def __init__(self):
        pass

    def loop(self):
        #print("Main loop running...")
        pass
        

if __name__ == "__main__":
    main = Main()
    app = PygameApp(main)


    points = []

    # 8 Ecken eines Würfels
    coords = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 1),
        (0, 1, 1),
    ]

    size = 200
    offset_x = 1000
    offset_y = 300
    for x, y, z in coords:
        points.append(vector.Vector3D(offset_x + x * size, offset_y + y * size, z * size*0.5))

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), 
        (4, 5), (5, 6), (6, 7), (7, 4),  
        (0, 4), (1, 5), (2, 6), (3, 7)  
    ]

    for a, b in edges:
        points[a].conect(points[b])



    app.set_points(points)
    app.loop() + self.pos[3].x
