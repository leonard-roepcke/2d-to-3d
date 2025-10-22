import pygame
import vector

class PygameApp:
    def __init__(self, main):
        self.main = main
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Meine App")
        self.running = True

        self.points = []


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            
            for point in self.points:
                pygame.draw.circle(self.screen, (255, 255, 255), (int(point.x), int(point.y)), 5)
            
            self.main.loop()
            pygame.display.flip()
        pygame.quit()
    
    def add_point(self, point):
        self.points.append(point)
