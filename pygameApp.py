import pygame
import vector

class PygameApp:
    def __init__(self, main):
        self.main = main
        pygame.init()
        self.screen = pygame.display.set_mode((2800, 1600))
        pygame.display.set_caption("Meine App")
        self.running = True

        self.points = []
        self.pos = [
            vector.Vector3D(1,0,0),
            vector.Vector3D(0,1,0),
            vector.Vector3D(0,0,1)
        ]


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            
            for point in self.points:
                point_2D = point.convert_to_2d()
                pygame.draw.circle(self.screen, (255, 255, 255), (int(point_2D.x), int(point_2D.y)), 5)
                for line in point.conections:
                    line_2D = line.convert_to_2d()
                    pygame.draw.line(self.screen, (255, 255, 255), (int(point_2D.x),int(point_2D.y)),(int(line_2D.x),int(line_2D.y)), 3)
            
            self.main.loop()
            pygame.display.flip()
        pygame.quit()
    
    def set_points(self, points):
        self.points = points

    def add_point(self, point):
        self.points.append(point)
