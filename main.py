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
    for i in range(100):
        points.append(vector.Vector3D(random.randint(0, 800),random.randint(0, 800),random.randint(0, 800)))
        if i > 0:
            points[-1].conect(random.choice(points[:-1]))




    app.set_points(points)
    app.loop()
