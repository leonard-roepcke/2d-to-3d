import pygameApp
import sys
import main


class PygameApp:
    def __init__(self):
        # --- Initialisierung ---
        pygameApp.init()
        programm = main.Main()

        # --- Fenster erstellen ---
        WIDTH, HEIGHT = 800, 600
        screen = pygameApp.display.set_mode((WIDTH, HEIGHT))
        pygameApp.display.set_caption("Mein Pygame-Programm")

        # --- Hauptloop ---
        clock = pygameApp.time.Clock()
        running = True
        while running:
            # --- Ereignisse (Events) abfragen ---
            for event in pygameApp.event.get():
                if event.type == pygameApp.QUIT:
                    running = False

            # --- Logik / Updates ---
            # (z. B. Positionen berechnen, Kollisionen prüfen, usw.)
            programm.loop()
            # --- Zeichnen ---
            screen.fill((30, 30, 30))  # Hintergrundfarbe
            # (hier zeichnest du Objekte)

            pygameApp.display.flip()  # Bildschirm aktualisieren
            clock.tick(60)         # 60 FPS

        # --- Beenden ---
        pygameApp.quit()
        sys.exit()
