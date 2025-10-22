import vector
from pygameApp import PygameApp

class Main:
    def __init__(self):
        pass

    def loop(self):
        print("Main loop running...")
        

if __name__ == "__main__":
    main = Main()
    app = PygameApp(main)
    app.add_point(vector.Vector3D(150, 150, 3).convert_to_2d())
    app.add_point(vector.Vector3D(300, 150, 3).convert_to_2d())
    app.add_point(vector.Vector3D(300, 300, 3).convert_to_2d())
    app.add_point(vector.Vector3D(300, 300, 50).convert_to_2d())
    app.loop()
