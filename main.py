import vector
from pygameApp import PygameApp

class Main:
    def __init__(self):
        v = vector.Vector3D(3, 4, 5)
        v2d = v.convert_to_2d()
        print("3D Vector Length:", v.get_length())
        print("Projected 2D Vector Length:", v2d.get_length())

    def loop(self):
        print("Main loop running...")
        

if __name__ == "__main__":
    main = Main()
    app = PygameApp(main)
